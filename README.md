# Deep-RSAEncryption-Script
A script that encrypts files (RSA encryption) in the current directory (folders content included), and jumps back into the previous directory to do the same. The script stops when it reaches a limit directory.<br />

1/Install the cryptopydome package (pip3 install -r requirements.txt)<br />
2/The script won't encrypt files unless you enable line 74. The variable 'LimitDir' in line 121 represents the directory that the script won't explore and also won't exceed to explore higher directories.<br /><br />



Caution!!! Files could be irreversebly lost. Execute at your own risk.
