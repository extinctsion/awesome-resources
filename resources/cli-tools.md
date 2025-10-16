# Useful Command-line Tools to learn

1. curl - 
   - A tool to transfer data from or to a server using various protocols (HTTP, HTTPS, FTP, etc.)
   - Commonly used to test APIs or download files
   - Code Ex - 
     - *Fetch a website :* `curl https://example.com`
  
2. wget - 
   - A non-interactive tool for downloading files from the web
   - Supports recursive downloads, making it useful for mirroring entire websites
   - Code Ex -
     - *Download a single file :* `wget https://example.com/file.zip`
  
3. fzf - 
   - A command-line fuzzy finder
   - Lets you quickly search and filter through files, directories, git commits, processes, etc
   - Code Ex - 
     - *Search through files in current directory :* `ls | fzf`

4. tldr - 
   - Provides simplified and community-driven explanations of command usage
   - Great for quickly recalling how to use rarely-used commands
   - Code Ex - 
     - *Install and check usage :* `tldr curl` > `tldr tar` > `tldr git checkout`

5. htop - 
   - An interactive process viewer and system monitor
   - Shows CPU, memory usage, and running processes in a more user-friendly way than top
   - Code Ex - 
     - *Start htop :* `htop`

6. jq – JSON processor - 
   - Parse, filter, and manipulate JSON easily
   - Code Ex - 
     - *Pretty-print JSON :* `curl https://api.github.com/users/octocat | jq .`

7. ncdu – Disk usage analyzer - 
   - Helps you explore disk space usage interactively
   - Code Ex - 
     - *Start ncdu in current directory :* `ncdu`
     - *Check disk usage of /var/log :* `ncdu /var/log`