class Time:
    "represents a specific time"
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    def details(self):
        print(f'{self.hour}:{self.minute}:{self.second}')

    def add_time(self,hour,minute,second):
        self.hour += hour
        self.minute += minute
        self.second += second
        print(self.hour,self.minute,self.second)

    def is_after(time1, time2):
        if time1.hour > time2.hour:
            return True
        elif time1.hour == time2.hour:
            if time1.minute > time2.minute:
                return True
            elif time1.minute == time2.minute:
                if time1.second > time2.second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def append_time(self,timeobj):
        """
            accepts a timeobject and increment the current time hour,min, and sec with the new time hour min and sec 
        """
        self.hour += timeobj.hour
        self.minute += timeobj.minute
        self.second += timeobj.second
        print(self.hour,self.minute,self.second)

    def add_time_v1(self,minute,second):
        """
            adds minute and seconds to the current time.
            Once minute reach 60,the hour should be incremented by one
            Once sec reach 60, the min should be incremented by one

        """
        self.minute += minute
        self.second += second

        if self.second == 60:
            self.minute += 1
        elif self.second > 60:
            self.minute += 1
            x = self.second - 60
            self.second = x
        if self.minute == 60:
            self.hour += 1
        elif self.minute > 60:
            self.hour += 1
            y = self.minute - 60
            self.minute = y
       
        print(self.hour,self.minute,self.second)
        
    def to_sec(self):
        y = self.minute * 60
        x = self.hour *3600
        result = x + y + self.second
        print(result)

t1 = Time(11,59,59)
t2 = Time(12,47,58)
t3 = Time(2,3,5)

print(t1.hour)