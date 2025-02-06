import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def fetch_url(url, output,element, html_output):   
    url = url.replace('\n', '')
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        #print(f"Error: Failed to send request to the URL {url}: {e}")
        sys.exit(1)
    for data in response.text.split('\n'):
         for elem in element.split(','):
            if elem in data:
                if 'X-Frame-Options' not in response.headers:
                    print('VULNERABLE TO CLICKJACKING: {0}'.format(url))
                    open(output, 'a').write(f"{url}\n")
                    if html_output != '':
                            open(html_output,'a').write(f'<h1>{url}</h1><br><br><iframe src="{url}">{url}</iframe><br/>\n')

            else:
                pass
         

def start_script():
    
    html = ''
    elements = ''
    output = ''
    save = ''
    args = sys.argv[1:]
    if not args:
            help_command()
            sys.exit(1)
    if '-o' not in args or '--output' not in args:
            output = 'click_sniper'
    if '-e' not in args or '--element' not in args:
            elements = ''
    if '-hm' not in args or '--html' not in args:
            html = ''
    val = 0
    for arg in args:
            if arg.startswith("--") or arg.startswith("-"):
                option_name = arg[2:] if arg.startswith("--") else arg[1:]
                if option_name == "help" or option_name == "h":
                    help_command()
                    sys.exit(0)
                elif option_name == "list" or option_name == "l":
                    try:
                        list_of_dir = args[val + 1]
                        list_of_dir = open(list_of_dir, 'r', encoding="ISO-8859-1").readlines()
                    except Exception as e:
                        print(f"Error: Could not open file {save}: {e}")
                        sys.exit(1)
                elif option_name == "element" or option_name == "e":
                    elements = args[val + 1]
                elif option_name == "output" or option_name == "o":
                    try:
                        output = args[val + 1]
                        open(output, 'w').write('')
                    except Exception as e:
                        print(f"Error: Could not open file {save}: {e}")
                        sys.exit(1)
                elif option_name == "html" or option_name == "hm":
                    
                    try:
                        html = args[val + 1]
                        open(html, 'w').write('')
                    except Exception as e:
                        print(f"Error: Could not open file {save}: {e}")
                        sys.exit(1)


                else:
                    print(f"Unknown option: {option_name}")
                    sys.exit(1)
            val = val + 1
    attack(list=list_of_dir,output=output,element=elements,html_output=html)


def help_command():
    print("Usage: %s [options]")
    print("Options:")
    print("  -h, --help           Display this help message")
    print("  -e, --element        Look for some element in the page, like inputs. EX: <input type=password (this indicates that the page has sensitive input fields) separe by commas")
    print("  -l, --list           Path to the list of directories")
    print("  -o, --output         Path to the save output file")
    print("  -hm, --html           Path to the HTML output file (This can be used as a PoC, beacuse it will create iframes to display the results)")



def attack(list, output, element, html_output):
    with ThreadPoolExecutor(max_workers=40) as executor:
        future_to_url = {executor.submit(fetch_url, url, output, element, html_output): url for url in list}
        for future in as_completed(future_to_url):
            url = future_to_url[future]  


start_script()


