read input
	if [[ $input ]] && [ $input -eq $input 2>/dev/null ] && [ $input >= 1024 && $input <= 65535]
		find / -name "sshd config" -print
		
		echo "Enter name: "
		read name
		sudo vi /etc/ssh/sshd_config
		Port $input
		
		sudo mv /etc/securetty /etc/securetty.orig
		sudo touch /etc/securetty
		sudo chmod 600 /etc/securetty