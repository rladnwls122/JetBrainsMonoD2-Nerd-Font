# JetBrainsMonoD2 Nerd Font - Terminal Ligature & Glyph Showcase
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$C_CYAN    = "`e[36m"
$C_GREEN   = "`e[32m"
$C_YELLOW  = "`e[33m"
$C_BLUE    = "`e[34m"
$C_MAGENTA = "`e[35m"
$C_RED     = "`e[31m"
$C_BOLD    = "`e[1m"
$C_DIM     = "`e[2m"
$C_RESET   = "`e[0m"

function Print-Header($title) {
    Write-Host ""
    Write-Host "$C_BOLD$C_CYAN┌─────────────────────────────────────────────────────────────┐$C_RESET"
    Write-Host "$C_BOLD$C_CYAN│  $title $((' ' * (57 - $title.Length)))│$C_RESET"
    Write-Host "$C_BOLD$C_CYAN└─────────────────────────────────────────────────────────────┘$C_RESET"
}

function Print-Section($name) {
    Write-Host "$C_BOLD$C_YELLOW  ▸ $name$C_RESET"
}

Clear-Host
Write-Host "$C_BOLD$C_MAGENTA"
Write-Host "   ╦╔═╗╔╦╗╔╗ ╦═╗╔═╗╦╔╗╔╔═╗  ╔╦╗╔═╗  ╔╗╔╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔╗╔╔╦╗"
Write-Host "   ║║╣  ║ ╠╩╗╠╦╝╠═╣║║║║╚═╗   ║║╚═╗  ║║║║╣ ╠╦╝ ║║  ╠╣ ║ ║║║║ ║ "
Write-Host "  ╚╝╚═╝ ╩ ╚═╝╩╚═╩ ╩╩╝╚╝╚═╝  ═╩╝╚═╝  ╝╚╝╚═╝╩╚══╩╝  ╚  ╚═╝╝╚╝ ╩ "
Write-Host "        JetBrains Mono + D2Coding + Nerd Font v3 Showcase       "
Write-Host "$C_RESET"

# 1. Language Ligatures
Print-Header "1. Programming Language Ligatures"

Print-Section "C / C++ / Java / C#"
Write-Host "     $C_GREEN==  !=  <=  >=  ++  --  +=  -=  *=  /=$C_RESET"
Write-Host "     $C_GREEN&&  ||  <<  >>  ->  ::  /* */  ///  <=$C_RESET"
Write-Host ""

Print-Section "JavaScript / TypeScript"
Write-Host "     $C_GREEN===  !==  =>  ?.  ??  ??=  &&=  ||=  <!-- -->$C_RESET"
Write-Host "     $C_GREEN${variable}  () => { return a !== b && c ??= 10; }$C_RESET"
Write-Host ""

Print-Section "Python"
Write-Host "     $C_GREEN->  :=  ==  !=  <=  >=  +=  -=  *=  /=  **  //$C_RESET"
Write-Host "     $C_GREENdef parse(data: dict) -> bool: return (x := val) != None$C_RESET"
Write-Host ""

Print-Section "Rust / Go / Functional (Elm, Haskell, F#)"
Write-Host "     $C_GREEN->  =>  ::  ..  ..=  <-  :=  |>  <|  <$>  <*>$C_RESET"
Write-Host "     $C_GREENmatch val { Ok(v) => v, Err(_) => panic!(\"error\") }$C_RESET"
Write-Host ""

Print-Section "Shell / Bash / Markdown"
Write-Host "     $C_GREEN&&  ||  |||  >>  <<  $(cmd)  ${ENV_VAR}  ## Header$C_RESET"
Write-Host "     $C_GREENcat << 'EOF' > output.log && echo \"Done!\" || exit 1$C_RESET"

# 2. Nerd Font Icons
Print-Header "2. Nerd Font Developer Icons (v3)"

Write-Host "  $C_CYAN[Git/VCS]$C_RESET        Git    Branch    Commit    Merge    Pull-Req  󰊢  Fork  󰘬  Stash"
Write-Host "  $C_BLUE[Platforms]$C_RESET      Windows    Arch    Debian    Fedora    Linux    macOS    Docker"
Write-Host "  $C_YELLOW[Cloud/DevOps]$C_RESET   K8s    Docker  󱂢  AWS  󰠅  GCP  󰠢  Azure  󱁢  Terraform  󱪿  Ansible"
Write-Host "  $C_MAGENTA[Languages]$C_RESET      Python    TypeScript    C++    Rust    Go    Java    React"
Write-Host "  $C_GREEN[Status]$C_RESET       ✔  Success  ✖  Error  ⚠  Warning  ℹ  Info  󰔟  Time    Clock  󰑮  Sync"

# 3. Korean & Monospace 1:2 Alignment
Print-Header "3. Korean (D2Coding) 1:2 Monospace Grid Test"

Write-Host "$C_DIM  Ruler (Latin x2 = Hangul x1):$C_RESET"
Write-Host "  $C_YELLOW|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|$C_RESET"
Write-Host "  $C_GREEN|일|이|삼|사|오|육|칠|팔|구|십|하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|스물|$C_RESET"
Write-Host "  $C_CYAN|AA|BB|CC|DD|EE|FF|GG|HH|II|JJ|KK|LL|MM|NN|OO|PP|QQ|RR|SS|TT|$C_RESET"
Write-Host ""
Write-Host "  $C_BOLD한글 샘플:$C_RESET 가나다라마바사 아자차카타파하 1234567890 !@#$`%^&*()"
Write-Host "  $C_BOLD문장 테스트:$C_RESET 동해 물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세"
Write-Host "  $C_BOLD호환 자모:$C_RESET ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ"

# 4. Mixed Real Code Sample
Print-Header "4. Real-world Code Sample"

Write-Host "$C_MAGENTA"
Write-Host "  async function fetchDeveloperStatus(userId: string): Promise<DevReport> {"
Write-Host "      // 🚀 한글 주석과 프로그래밍 리가처 & Nerd Font 아이콘 조화"
Write-Host "      const user = await db.users.findUnique({ where: { id: userId } });"
Write-Host "      if (!user || user.status !== 'ACTIVE') {"
Write-Host "          logger.warn(`⚠ 사용자 [${userId}] 정보를 찾을 수 없습니다.`);"
Write-Host "          return { ok: false, error: 'USER_NOT_FOUND' };"
Write-Host "      }"
Write-Host "      const score = (user.commits ?? 0) * 1.5 + (user.prs ?? 0) * 2.0;"
Write-Host "      return { ok: true, score: score >= 100 ? '󰘬 MASTER' : '󰊢 JUNIOR' };"
Write-Host "  }"
Write-Host "$C_RESET"
Write-Host ""
