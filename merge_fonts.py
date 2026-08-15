import os
import zipfile
import io
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.misc.transform import Transform

def extract_and_load_fonts():
    os.makedirs("build", exist_ok=True)
    with zipfile.ZipFile("JetBrainsMono.zip", "r") as z:
        z.extract("JetBrainsMonoNerdFont-Regular.ttf", "build")
        z.extract("JetBrainsMonoNerdFont-Bold.ttf", "build")
        z.extract("JetBrainsMonoNerdFont-Italic.ttf", "build")
        z.extract("JetBrainsMonoNerdFont-BoldItalic.ttf", "build")
    print("Extracted JetBrains Mono Nerd Font files.")

def get_korean_codepoints(d2_font):
    cmap = d2_font.getBestCmap()
    korean_ranges = [
        (0xAC00, 0xD7AF),  # Hangul Syllables
        (0x3130, 0x318F),  # Hangul Compatibility Jamo
        (0x1100, 0x11FF),  # Hangul Jamo
        (0xA960, 0xA97F),  # Hangul Jamo Extended-A
        (0xD7B0, 0xD7FF),  # Hangul Jamo Extended-B
        (0x3200, 0x321E),  # Enclosed CJK Letters (Parenthesized Hangul)
        (0x3260, 0x327E),  # Enclosed CJK Letters (Circled Hangul)
        (0x3000, 0x303F),  # CJK Symbols and Punctuation (e.g. ideographic space)
        (0xFF01, 0xFF60),  # Fullwidth ASCII variants / punctuation
    ]
    
    selected_cps = set()
    for start, end in korean_ranges:
        for cp in range(start, end + 1):
            if cp in cmap:
                selected_cps.add(cp)
    return selected_cps

def update_name_table(font, family_name, subfamily_name):
    name_table = font['name']
    full_name = f"{family_name} {subfamily_name}"
    ps_name = f"{family_name.replace(' ', '')}-{subfamily_name.replace(' ', '')}"
    unique_id = f"1.000;AGY;{ps_name}"
    
    target_ids = {1, 2, 3, 4, 6, 16, 17, 21, 22}
    name_table.names = [r for r in name_table.names if r.nameID not in target_ids]
    
    platforms = [(3, 1, 0x409), (1, 0, 0)]
    for pid, eid, lid in platforms:
        name_table.setName(family_name, 1, pid, eid, lid)
        name_table.setName(subfamily_name, 2, pid, eid, lid)
        name_table.setName(unique_id, 3, pid, eid, lid)
        name_table.setName(full_name, 4, pid, eid, lid)
        name_table.setName(ps_name, 6, pid, eid, lid)
        name_table.setName(family_name, 16, pid, eid, lid)
        name_table.setName(subfamily_name, 17, pid, eid, lid)

def merge_font_pair(base_path, d2_path, output_path, family_name, subfamily_name, is_italic=False):
    print(f"\nMerging {base_path} + {d2_path} -> {output_path}...")
    base_font = TTFont(base_path)
    d2_font = TTFont(d2_path)
    
    korean_cps = get_korean_codepoints(d2_font)
    print(f"Total Korean/CJK codepoints to import: {len(korean_cps)}")
    
    d2_cmap = d2_font.getBestCmap()
    d2_glyph_set = d2_font.getGlyphSet()
    
    base_glyf = base_font['glyf']
    base_hmtx = base_font['hmtx']
    base_glyph_order = list(base_font.getGlyphOrder())
    
    target_hangul_width = 1200
    scale_factor = 1.15
    dx = (target_hangul_width - (1000 * scale_factor)) / 2.0  # 25.0
    dy = -15.0  # visual baseline alignment
    
    if is_italic:
        slant = 0.20  # ~11 deg slant for italic
        transform = Transform(scale_factor, 0, slant, scale_factor, dx, dy)
    else:
        transform = Transform(scale_factor, 0, 0, scale_factor, dx, dy)
    
    added_glyphs_count = 0
    cp_to_glyph_map = {}
    
    for cp in sorted(korean_cps):
        d2_glyph_name = d2_cmap[cp]
        new_glyph_name = f"hangul_u{cp:04X}"
        
        # Decompose any composite glyphs into raw contours
        rec_pen = DecomposingRecordingPen(d2_glyph_set)
        t_pen = TransformPen(rec_pen, transform)
        d2_glyph_set[d2_glyph_name].draw(t_pen)
        
        # Build glyph
        pen = TTGlyphPen(glyphSet=None)
        rec_pen.replay(pen)
        new_glyph = pen.glyph()
        
        base_glyf[new_glyph_name] = new_glyph
        
        lsb = getattr(new_glyph, 'xMin', int(dx))
        base_hmtx[new_glyph_name] = (target_hangul_width, lsb)
        
        base_glyph_order.append(new_glyph_name)
        cp_to_glyph_map[cp] = new_glyph_name
        added_glyphs_count += 1

    base_font.setGlyphOrder(base_glyph_order)
    
    for table in base_font['cmap'].tables:
        if table.isUnicode():
            for cp, gname in cp_to_glyph_map.items():
                table.cmap[cp] = gname
                
    os2 = base_font['OS/2']
    os2.ulCodePageRange1 |= (1 << 19)
    os2.ulUnicodeRange1 |= (1 << 28)
    os2.ulUnicodeRange2 |= (1 << 23)
    
    update_name_table(base_font, family_name, subfamily_name)
    
    base_font.save(output_path)
    print(f"Successfully created {output_path} with {added_glyphs_count} merged Korean glyphs.")

def main():
    extract_and_load_fonts()
    family_name = "JetBrainsMonoD2 Nerd Font"
    
    # 1. Regular
    merge_font_pair(
        base_path="build/JetBrainsMonoNerdFont-Regular.ttf",
        d2_path="D2CodingLigature/D2Coding-Ver1.3.3-20260725-ligature.ttf",
        output_path="build/JetBrainsMonoD2NerdFont-Regular.ttf",
        family_name=family_name,
        subfamily_name="Regular"
    )
    
    # 2. Bold
    merge_font_pair(
        base_path="build/JetBrainsMonoNerdFont-Bold.ttf",
        d2_path="D2CodingLigature/D2CodingBold-Ver1.3.3-20260725-ligature.ttf",
        output_path="build/JetBrainsMonoD2NerdFont-Bold.ttf",
        family_name=family_name,
        subfamily_name="Bold"
    )
    
    # 3. Italic
    merge_font_pair(
        base_path="build/JetBrainsMonoNerdFont-Italic.ttf",
        d2_path="D2CodingLigature/D2Coding-Ver1.3.3-20260725-ligature.ttf",
        output_path="build/JetBrainsMonoD2NerdFont-Italic.ttf",
        family_name=family_name,
        subfamily_name="Italic",
        is_italic=True
    )
    
    # 4. Bold Italic
    merge_font_pair(
        base_path="build/JetBrainsMonoNerdFont-BoldItalic.ttf",
        d2_path="D2CodingLigature/D2CodingBold-Ver1.3.3-20260725-ligature.ttf",
        output_path="build/JetBrainsMonoD2NerdFont-BoldItalic.ttf",
        family_name=family_name,
        subfamily_name="Bold Italic",
        is_italic=True
    )
    
    print("\nAll 4 font styles created successfully!")

if __name__ == "__main__":
    main()
