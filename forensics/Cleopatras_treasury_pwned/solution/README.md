Once you've downloaded the archive, you can extract the files using:

```
tar -xzf archive.tar.gz
```

Q1: What is the first command the attacker ran on the machine?
Its the first command in th .zsh_history file
A: `woami`

Q2: The attacker executed 4 commands for enumeration purposes including whoami. The last one displays files with a special permission bit, what is that bit called?Format: Name bit
The last enumeration command the attacker ran was: `find / -perm /4000 -type f 2>/dev/null`
which through some research you'll be able to tell is used to find files with SUID bit on the machine
A: `SUID bit`

Q3: What is the name of the executable that was exploited?
The attacker started investigating treasury after running the previous command to exploit it. Even gdb was used to reverse engineer the binary
A: `treasury`

Q4: The exploit used Buffer Overflow vulnerability to enter a locked function in the treasury file, what was the size of the buffer?
From the exploit script the attacker left on the machine we could see 5g 'a's being sent 
A: `56`

Q5: Provide the exact timestamp for when the attacker successfully opened a root shell by exploiting treasury executable. Format: YYYY-MM-DD HH:MM:SS-HH:00
From syslog in the `/var/log` directory, if we search for the word treasury the timestamps of when it was executed will appear. The log that shows treasury laucning `/bin/sh` is the log we are looking for
A: `2024-09-26 17:45:48-04:00`

Q6: To maintain persistence, the attacker created a new user with root privileges. What was the username?
Looking in auth.log for the useradd command, we find the user yasta being created less than a minute after the attacker lauched a shell from treasury
A: `yasta`
