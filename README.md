# Todo

* [] Refresh
  * Refresh
  ` $ adb shell input swipe 540 1110 540 2000 150`
  * This will start at x:540 y:1110 and end at x:540 y:2000 in 150ms
  * Since ` $ adb shell wm size` gives size as 1080x2220
~~* [] Send screenshot to PC for processing~~
  ~~* ` $ adb exec-out screencap -p > screen.png`~~
  ~~* Creates a file calles screen.png on my computer~~
~~* [] Read screenshot looking for given text~~
* [] Create xml of whats on screen
  * ` $ adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /tmp/view.xml`
* [] Click on accept or decline for all jobs
  * Claiming jobs
  * Declining Jobs
    * ` $ perl -ne 'printf "%d %d\n", ($1+$3)/2, ($2+$4)/2 if /text="Decline"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"/' /tmp/view.xml`
    * Finds midpoint of decline button
    * ` $ adb shell input tap 371 848`
