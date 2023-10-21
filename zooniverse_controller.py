import mouse as ms
import keyboard as kbd
import time

yes_key = "y"
no_key = "n"
done_key = "x"
done_and_talk_key = "z"
play_pause_key = "p"
stats_key = "s"
quit_key = "q"
close_popup_key = "c"
stop_script_key = "k"
resume_script_key = "m"

print("Zooniverse Web Interface Keyboard Controller")
print("\nControls:")
print(yes_key, "- Mark YES")
print(no_key, "- Mark NO")
print(close_popup_key, "- Close Popup")
print(done_key, "- Done")
print(done_and_talk_key, "- Done & Talk")
print(play_pause_key, "- Play/Pause Sequence")
print(stats_key, "- Show My YES Percentage")
print(quit_key, "- Quit This Program")
print(stop_script_key, "- Disable Controls (stops keyboard keys from controlling your mouse but does not quit the program)")
print(resume_script_key, "- Enable Controls")
print("\nTo calibrate the positions of the buttons, hold Shift, bring your mouse cursor onto the button on the webpage and press the keyboard key you want to assign to that button.\n\n")

yes = 0
no = 0

yes_pos = [1200, 530]
no_pos = [1200, 600]
play_pause_pos = [475, 950]
done_and_talk_pos = [1150, 720]
done_pos = [1350, 720]
close_popup_pos = [0, 540]

current_selection = None
running = True
controls_enabled = True
while running:

    if controls_enabled:

        if not kbd.is_pressed("Shift"):
                
            if kbd.is_pressed(yes_key):
                ms.move(yes_pos[0], yes_pos[1], absolute=True)
                ms.click()
                current_selection = "yes"
                time.sleep(0.05)

            elif kbd.is_pressed(no_key):
                ms.move(no_pos[0], no_pos[1], absolute=True)
                ms.click()
                current_selection = "no"
                time.sleep(0.05)

            elif kbd.is_pressed(play_pause_key):
                ms.move(play_pause_pos[0], play_pause_pos[1], absolute=True)
                ms.click()
                time.sleep(0.05)

            elif kbd.is_pressed(done_and_talk_key):
                ms.move(done_and_talk_pos[0], done_and_talk_pos[1], absolute=True)
                ms.click()

                if current_selection == "yes":
                    yes += 1
                elif current_selection == "no":
                    no += 1

                current_selection == None
                time.sleep(0.05)

            elif kbd.is_pressed(done_key):
                ms.move(done_pos[0], done_pos[1], absolute=True)
                ms.click()

                if current_selection == "yes":
                    yes += 1
                elif current_selection == "no":
                    no += 1

                current_selection == None
                time.sleep(0.05)

            elif kbd.is_pressed(quit_key):
                running = False

            elif kbd.is_pressed(close_popup_key):
                ms.move(close_popup_pos[0], close_popup_pos[1], absolute=True)
                ms.click()

            elif kbd.is_pressed(stats_key):
                if yes + no > 0:
                    print("Your identification stats for this session:", yes/(yes+no) * 100, "% Yes")
                else:
                    print("You haven't made any classifications in this session so far!")
                time.sleep(0.1)

            elif kbd.is_pressed(stop_script_key):
                controls_enabled = False
                print("Controls disabled.")

        else:

            if kbd.is_pressed(yes_key):
                yes_pos = ms.get_position()
                print("New position assigned for YES key.")
                time.sleep(0.2)

            elif kbd.is_pressed(no_key):
                no_pos = ms.get_position()
                print("New position assigned for NO key.")
                time.sleep(0.2)

            elif kbd.is_pressed(play_pause_key):
                play_pause_pos = ms.get_position()
                print("New position assigned for Play/Pause key.")
                time.sleep(0.2)

            elif kbd.is_pressed(done_and_talk_key):
                done_and_talk_pos = ms.get_position()
                print("New position assigned for Done & Talk key.")
                time.sleep(0.2)

            elif kbd.is_pressed(done_key):
                done_pos = ms.get_position()
                print("New position assigned for Done key.")
                time.sleep(0.2)

            elif kbd.is_pressed(close_popup_key):
                close_popup_pos = ms.get_position()
                print("New position assigned for Close Popup key.")
                time.sleep(0.2)

    else:

        if kbd.is_pressed(resume_script_key):
            controls_enabled = True
            print("Controls enabled.")

print("Zooniverse Web Interface Keyboard Controller - PROGRAM QUIT")
