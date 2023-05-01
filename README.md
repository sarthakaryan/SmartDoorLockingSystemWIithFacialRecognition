# Smart Door Locking System With Facial Recognition

This project is a  Smart door-locking system that uses facial recognition. A user takes a picture of their face using an app on their smartphone, which is sent to a server for recognition. If the user is authorized, the system unlocks the door.

 
 



## Appendix

The door locking system we have created is a solution that relies on facial recognition, wireless communication, and microcontroller programming. The system provides a secure and convenient way for users to unlock a door by taking a picture of their face using a React Native app on their smartphone. The app then sends the picture to a backend server, which uses OpenCV libraries and Eigen face technique to recognize the user's face and determine whether they are authorized to enter. If the user is authorized, the server sends a signal wirelessly to an ESP32 microcontroller, which activates a servo motor to unlock the door. The ESP32 also displays the user's name on an LCD screen and provides a green indication to signal that the door has been successfully unlocked.

### Instrutions for use:
* Launch the app on your smartphone and take a clear picture of your face, ensuring that it is well-lit and that your entire face is visible in the designated area.
* Click the "Upload Photo" button to send the picture to the server for recognition.
* Wait for the server to process the picture and determine whether you are authorized to enter.
* If authorized, the ESP32 microcontroller will activate the servo motor to unlock the door, display your name on the LCD screen, and provide a green indication.
* The door will remain open for a few seconds after unlocking and then lock automatically.
* If not authorized, the door will remain locked, and the ESP32 microcontroller will provide a red indication.

### Languages and Frameworks:
* Arduino programming
* Python
* Node.js
* React Native
* Expo

### Required Components:
* ESP32
* LEDs
* Resistor
* LCD 16x2
* Breadboard
* Jumpwires
* Servo Motor

### Circuit Diagram:
![image](https://user-images.githubusercontent.com/128975431/235454605-e4a109df-3a67-4a1a-8ca4-f186021b88f4.png)



## Screenshots
![image](https://user-images.githubusercontent.com/128975431/235454800-915de007-58c4-4d03-ac60-d07efa0c3a1d.png)

![image](https://user-images.githubusercontent.com/128975431/235454797-85a1f384-b002-47e1-bdce-f0619f015ddc.png)





## Authors

- [@sarthakaryan](https://github.com/sarthakaryan)
- [@RohanRJ389](https://github.com/RohanRJ389)

