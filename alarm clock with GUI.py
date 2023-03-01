from tkinter import *
import datetime
import time
import threading
import winsound

class AlarmClock:
    def __init__(self):
        self.clock = Tk()
        self.clock.title("Alarm Clock")
        self.clock.geometry("400x200")
        self.stop_alarm = False
        self.alarm_thread = None

        time_format = Label(self.clock, text="Note: Enter time in 24 hour format", fg="red", bg="black", font="Arial")
        time_format.place(x=60, y=120)

        add_time = Label(self.clock, text="Hour  Min   Sec", font=60)
        add_time.place(x=110)

        set_alarm = Label(self.clock, text="Enter the time", fg="blue", relief="solid", font=("Helvetica", 10, "bold"))
        set_alarm.place(x=0, y=29)

        self.hour = StringVar()
        self.min = StringVar()
        self.sec = StringVar()

        hour_time = Entry(self.clock, textvariable=self.hour, bg="pink", width=15)
        hour_time.place(x=110, y=30)
        min_time = Entry(self.clock, textvariable=self.min, bg="pink", width=15)
        min_time.place(x=150, y=30)
        sec_time = Entry(self.clock, textvariable=self.sec, bg="pink", width=15)
        sec_time.place(x=200, y=30)

        set_button = Button(self.clock, text="Set Alarm", fg="red", width=10, command=self.set_alarm)
        set_button.place(x=110, y=70)

        snooze_button = Button(self.clock, text="Snooze", fg="blue", command=lambda: self.snooze(10))
        snooze_button.place(x=200, y=70)


        stop_button = Button(self.clock, text="Stop", fg="blue", command=self.stop_alarm_sound)
        stop_button.place(x=260, y=70)

        self.clock.mainloop()       

    def run_alarm_thread(self):
        set_alarm_timer = f"{self.hour.get()}:{self.min.get()}:{self.sec.get()}"
        while True:
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            print("The Set Date is:", date)
            print(now)
            if self.stop_alarm:
                break
            if now == set_alarm_timer:
                print("Time to Wake up")
                self.play_alarm_sound()
                time.sleep(1)
                break
            else:
                time.sleep(1)

    def set_alarm(self):
        if self.alarm_thread is None or not self.alarm_thread.is_alive():
            self.stop_alarm = False
            self.alarm_thread = threading.Thread(target=self.run_alarm_thread)
            self.alarm_thread.start()
            

    def play_alarm_sound(self):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

    def stop_alarm_sound(self):
        self.stop_alarm = True
        try:
            winsound.PlaySound(None, winsound.SND_ASYNC)
        except TypeError:
            winsound.PlaySound(None, winsound.SND_ASYNC)

    def snooze(self, seconds):
        print(f"Snoozing for {seconds} seconds")
        self.stop_alarm_sound()
        self.clock.after(seconds * 1000, self.play_alarm_sound)
        self.clock.after((seconds + 1) * 1000, self.set_alarm)

                
if __name__ == '__main__':
    AlarmClock()