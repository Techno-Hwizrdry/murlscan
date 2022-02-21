$GITTEMP=".\.gitignore_temp"
$PYTHON3=(Get-Command python).Path

Rename-Item .\.gitignore $GITTEMP
virtualenv -p $PYTHON3 .
Remove-Item .\.gitignore
Rename-Item $GITTEMP .gitignore
Copy-Item .\murlscan.conf_example -Destination .\murlscan.conf
.\Scripts\activate
pip3 install -r requirements.txt
deactivate