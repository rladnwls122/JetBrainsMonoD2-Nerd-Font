from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import os

def verify_font(font_path):
    print(f"=== Verifying {font_path} ===")
    f = TTFont(font_path)
    cmap = f.getBestCmap()
    hmtx = f['hmtx']
    
    # 1. Total glyphs & UPM
    print(f"Units Per Em: {f['head'].unitsPerEm}")
    print(f"Total glyphs in font: {len(f.getGlyphOrder())}")
    
    # 2. Check ASCII 'A'
    ascii_a_cp = ord('A')
    assert ascii_a_cp in cmap, "Missing ASCII 'A'"
    ascii_a_width = hmtx[cmap[ascii_a_cp]][0]
    print(f"ASCII 'A' advance width: {ascii_a_width}")
    
    # 3. Check Hangul '가' (0xAC00) & '힣' (0xD7A3)
    ga_cp = ord('가')
    assert ga_cp in cmap, "Missing Hangul '가'"
    ga_width = hmtx[cmap[ga_cp]][0]
    print(f"Hangul '가' advance width: {ga_width}")
    assert ga_width == 1200, f"Expected 1200 width for Hangul, got {ga_width}"
    assert ascii_a_width == 600, f"Expected 600 width for Latin, got {ascii_a_width}"
    
    # 4. Check total Hangul syllables count
    hangul_syllables = [cp for cp in range(0xAC00, 0xD7A4) if cp in cmap]
    print(f"Hangul Syllables count: {len(hangul_syllables)} / 11172")
    assert len(hangul_syllables) == 11172, "Missing some Hangul syllables"
    
    # 5. Check Nerd Font Icons (e.g. U+E702 / U+E781 / U+F113 / U+E0A0 etc.)
    nf_icons = [0xE702, 0xF113, 0xE0A0, 0xF007]
    found_nf = [hex(cp) for cp in nf_icons if cp in cmap]
    print(f"Nerd Font sample icons found: {found_nf}")
    
    # 6. Check GSUB (Ligatures)
    has_gsub = 'GSUB' in f
    print(f"GSUB table present (Ligatures): {has_gsub}")
    
    print("Verification Passed!\n")

def render_sample_image():
    font_path = "build/JetBrainsMonoD2NerdFont-Regular.ttf"
    bold_path = "build/JetBrainsMonoD2NerdFont-Bold.ttf"
    
    font_size = 28
    font_reg = ImageFont.truetype(font_path, font_size)
    font_bold = ImageFont.truetype(bold_path, font_size)
    
    img = Image.new("RGB", (1100, 600), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)
    
    lines = [
        ("JetBrainsMonoD2 Nerd Font (Regular & Bold)", font_bold, (100, 200, 255)),
        ("가나다라마바사 아자차카타파하 1234567890", font_reg, (240, 240, 240)),
        ("동해 물과 백두산이 마르고 닳도록 하느님이 보우하사", font_reg, (220, 220, 220)),
        ("Quick brown fox jumps over the lazy dog.", font_reg, (180, 220, 180)),
        ("def calculate_metrics(values: list[int]) -> bool:", font_reg, (255, 198, 109)),
        ("    if a != b and c >= d and e == f:  # Ligatures: !=, >=, ==", font_reg, (169, 183, 198)),
        ("        return (한글_테스트 and True) => /* 리가처 & 한글 */", font_reg, (152, 118, 170)),
        ("한글과 영문의 완벽한 2:1 고정폭 모노스페이스 정렬 테스트", font_bold, (255, 198, 109)),
        ("01234567890123456789012345678901234567890123456789", font_reg, (120, 120, 120)),
        ("일이삼사오육칠팔구십일이삼사오육칠팔구십일이삼사오", font_reg, (120, 120, 120)),
    ]
    
    y = 30
    for text, f, color in lines:
        draw.text((40, y), text, font=f, fill=color)
        y += 50
        
    os.makedirs("sample_output", exist_ok=True)
    img.save("sample_output/font_sample.png")
    print("Saved sample image to sample_output/font_sample.png")

if __name__ == "__main__":
    for font_file in [
        "build/JetBrainsMonoD2NerdFont-Regular.ttf",
        "build/JetBrainsMonoD2NerdFont-Bold.ttf",
        "build/JetBrainsMonoD2NerdFont-Italic.ttf",
        "build/JetBrainsMonoD2NerdFont-BoldItalic.ttf"
    ]:
        verify_font(font_file)
    render_sample_image()
