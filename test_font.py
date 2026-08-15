# -*- coding: utf-8 -*-
import sys

CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

def print_header(title):
    print()
    print(f"{BOLD}{CYAN}┌─────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{BOLD}{CYAN}│  {title:<55} │{RESET}")
    print(f"{BOLD}{CYAN}└─────────────────────────────────────────────────────────────┘{RESET}")

def print_section(name):
    print(f"{BOLD}{YELLOW}  ▸ {name}{RESET}")

def main():
    print(f"{BOLD}{MAGENTA}")
    print("   ╦╔═╗╔╦╗╔╗ ╦═╗╔═╗╦╔╗╔╔═╗  ╔╦╗╔═╗  ╔╗╔╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔╗╔╔╦╗")
    print("   ║║╣  ║ ╠╩╗╠╦╝╠═╣║║║║╚═╗   ║║╚═╗  ║║║║╣ ╠╦╝ ║║  ╠╣ ║ ║║║║ ║ ")
    print("  ╚╝╚═╝ ╩ ╚═╝╩╚═╩ ╩╩╝╚╝╚═╝  ═╩╝╚═╝  ╝╚╝╚═╝╩╚══╩╝  ╚  ╚═╝╝╚╝ ╩ ")
    print("        JetBrains Mono + D2Coding + Nerd Font v3 Showcase       ")
    print(f"{RESET}")

    # 1. Ligatures
    print_header("1. Programming Language Ligatures")
    
    print_section("C / C++ / Java / C#")
    print(f"     {GREEN}==  !=  <=  >=  ++  --  +=  -=  *=  /={RESET}")
    print(f"     {GREEN}&&  ||  <<  >>  ->  ::  /* */  ///  <={RESET}\n")

    print_section("JavaScript / TypeScript")
    print(f"     {GREEN}===  !==  =>  ?.  ??  ??=  &&=  ||=  <!-- -->{RESET}")
    print(f"     {GREEN}${{variable}}  () => {{ return a !== b && c ??= 10; }}{RESET}\n")

    print_section("Python")
    print(f"     {GREEN}->  :=  ==  !=  <=  >=  +=  -=  *=  /=  **  //{RESET}")
    print(f"     {GREEN}def parse(data: dict) -> bool: return (x := val) != None{RESET}\n")

    print_section("Rust / Go / Functional")
    print(f"     {GREEN}->  =>  ::  ..  ..=  <-  :=  |>  <|  <$>  <*>{RESET}")
    print(f"     {GREEN}match val {{ Ok(v) => v, Err(_) => panic!(\"error\") }}{RESET}\n")

    print_section("Shell / Bash / Markdown")
    print(f"     {GREEN}&&  ||  |||  >>  <<  $(cmd)  ${{ENV_VAR}}  ## Header{RESET}")
    print(f"     {GREEN}cat << 'EOF' > output.log && echo \"Done!\" || exit 1{RESET}")

    # 2. Nerd Font Icons
    print_header("2. Nerd Font Developer Icons (v3)")
    print(f"  {CYAN}[Git/VCS]{RESET}        Git    Branch    Commit    Merge    Pull-Req  󰊢  Fork  󰘬  Stash")
    print(f"  {BLUE}[Platforms]{RESET}      Windows    Arch    Debian    Fedora    Linux    macOS    Docker")
    print(f"  {YELLOW}[Cloud/DevOps]{RESET}   K8s    Docker  󱂢  AWS  󰠅  GCP  󰠢  Azure  󱁢  Terraform  󱪿  Ansible")
    print(f"  {MAGENTA}[Languages]{RESET}      Python    TypeScript    C++    Rust    Go    Java    React")
    print(f"  {GREEN}[Status]{RESET}       ✔  Success  ✖  Error  ⚠  Warning  ℹ  Info  󰔟  Time    Clock  󰑮  Sync")

    # 3. Korean 1:2 Alignment
    print_header("3. Korean (D2Coding) 1:2 Monospace Grid Test")
    print(f"{DIM}  Ruler (Latin x2 = Hangul x1):{RESET}")
    print(f"  {YELLOW}|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|{RESET}")
    print(f"  {GREEN}|일|이|삼|사|오|육|칠|팔|구|십|하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|스물|{RESET}")
    print(f"  {CYAN}|AA|BB|CC|DD|EE|FF|GG|HH|II|JJ|KK|LL|MM|NN|OO|PP|QQ|RR|SS|TT|{RESET}\n")
    print(f"  {BOLD}한글 샘플:{RESET} 가나다라마바사 아자차카타파하 1234567890 !@#$%^&*()")
    print(f"  {BOLD}문장 테스트:{RESET} 동해 물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세")
    print(f"  {BOLD}호환 자모:{RESET} ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ")

    # 4. Mixed Real Code Sample
    print_header("4. Real-world Code Sample")
    code = f"""{MAGENTA}
  async function fetchDeveloperStatus(userId: string): Promise<DevReport> {{
      // 🚀 한글 주석과 프로그래밍 리가처 & Nerd Font 아이콘 조화
      const user = await db.users.findUnique({{ where: {{ id: userId }} }});
      if (!user || user.status !== 'ACTIVE') {{
          logger.warn(`⚠ 사용자 [${{userId}}] 정보를 찾을 수 없습니다.`);
          return {{ ok: false, error: 'USER_NOT_FOUND' }};
      }}
      const score = (user.commits ?? 0) * 1.5 + (user.prs ?? 0) * 2.0;
      return {{ ok: true, score: score >= 100 ? '󰘬 MASTER' : '󰊢 JUNIOR' }};
  }}
{RESET}"""
    print(code)

if __name__ == "__main__":
    main()
