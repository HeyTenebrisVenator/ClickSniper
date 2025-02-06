# ClickSniper
ClickSniper is a tool that is developed with python, and it's mission is to transform the clickjacking hunt much easier

ClickJacking is one of the easiest vulnerabilities that you can find. It works with the iframe element from html, that can create an hidden fishing page

Options:
-h, --help           Display this help message
-e, --element        Look for some element in the page, like inputs. EX: <input type="password" (this indicates that the page has sensitive input fields) separe by commas
-l, --list           Path to the list of directories
-o, --output         Path to the save output file
-hm, --html           Path to the HTML output file (This can be used as a PoC, beacuse it will create iframes to display the results)

To do this tool works properly, you'll need to give it a file with directories.

!WARNING: THIS TOOL NEED THE ENTIRE URL, SUCH AS THE PROTOCOL!

EX: https://google.com/search

This tool can look for sensitive elements in the html. For example, an password input  -->  <input type="password">

The script will try to find this element in the html of the page, and try an clickjacking attack

To save the data, you can use the flag -o or --output

This'll save the data as text

But, you can save the data as html, and this will make an iframe automatically, so this can work as a PoC
