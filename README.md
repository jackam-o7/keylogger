# Python Keylogger
## Description
This project is focused on creating a simple keylogger in Kali Linux to capture and log keystrokes. Understanding how keyloggers function is essential for cybersecurity, enabling better protection against these types of attacks. My keylogger will be implemented using Python, taking advantage of Kali Linux's environment to simplify the process and avoid paltform-specific complications. The primary aim of this project is to gain hands-on experience with keyloggers, learning how they operate in real-world attacks. The knowledge gained will improve detection techniques and overall system security in professional environments.

## Languages and Utilities used
- Python
- VirtualBox
  

## Environments used
- Kali Linux

## Program walk-through
### Creating my python script
- To get started, I made sure Python was installed and up to date on my Kali Linux machine. </br>
- I also needed to install the pynput library, which allows me to control and monitor input devices. </br>

<img src="https://imgur.com/UzpTQj9.png" height="60%" width="60%" alt="installing python"/> 

<img src="https://imgur.com/pZx6KY8.png" height="60%" width="60%" alt="installing pynput library"/> <br/>

Now that everything was up-to-date and ready to go, I used the nano command to create the file in which my script would be written.
<img src="https://imgur.com/ANYHHxb.png" height="40%" width="40%" alt="using nano to create python script"/> <br/>
Nano is a command-line text editor and I used it here to create a new Python file called 'Keylogger.py', this allowed me to write and edit the code directly in the terminal environment, the script uses the pynput library to listen for keyboard events.
- My script defines a function to log each keystroke to a file named 'key_log.txt'. It formats the keystrokes, handling special keys appropriately.
- The keystrokes are appended to the log file, allowing for continuous recording of user input.
- The script sets up a listener that waits for key presses and calls the logging function accordingly. It includes a mechanism to stop the listener when the Escape key is pressed.

<img src="https://imgur.com/ImemZyo.png" height="60%" width="60%" alt="python script"/> <br/>

### Testing my python script
With my script written, I saved it using Ctrl + O and the next thing to do was test it! I ran the following command in my terminal to execute the script
- python3 keylogger.py </br>

<img src="https://imgur.com/3nq3TAl.png" height="40%" width="40%" alt="python script running, sending keystrokes to be logged"/> <br/>
Now that my script was running, I sent some keystrokes to my terminal so that I would be able to ensure that was actively recording my keystrokes in real time. After typing a sentence, I pressed the Escape key to stop the keylogger, which terminated the listener and halted the logging process.

<img src="https://imgur.com/ZX5iqz4.png" height="40%" width="40%" alt=" keystrokes repeated back in terminal"/> <img src="https://imgur.com/kNNcFCN.png" height="50%" width="50%" alt="keystrokes logged"/> <br/>
After exiting the script, the logged keys were both repeated back to me in the terminal, and saved to 'key_log.txt'. To review the captured keystrokes, I opened the key_log.txt file. I used the command cat key_log.txt to display its contents in the terminal. This allowed me to see all the recorded input, confirming that the keylogger successfully captured my keystrokes. I carefully checked the log file to ensure that it accurately reflected what I had typed, which was crucial for verifying that the keylogger worked as intended.
After some examination, I was pleased to find that everything had functioned correctly. The keylogger performed as expected, providing a valuable learning experience in understanding how such tools operate and the importance of cybersecurity awareness.

## Conclusion
In this project, I successfully created a keylogger in Kali Linux using Python and the pynput library. Through this process, I gained valuable insights into how keyloggers operate and how they can capture user input. The hands-on experience of writing, testing, and reviewing the script enhanced my understanding of keyboard event handling and logging mechanisms. </br> </br>
While this keylogger is relatively simple in its design, it serves as a foundational example of how keystroke logging works. This project has reinforced my awareness of cybersecurity challenges and the necessity of robust defenses against such threats. As I continue to explore this field, I look forward to expanding my knowledge by implementing more advanced features and techniques. Overall, this experience has been instrumental in deepening my understanding of cybersecurity and the importance of ethical considerations in technology. </br> </br>
Although keyloggers can be used maliciously, this projects purpose was that of education, underscoring the critical need for cybersecurity awareness and proactive measures to safeguard against potential risks. Moving forward, I plan to explore additional features and improvements to the keylogger, further expanding my knowledge in the field of cybersecurity.
