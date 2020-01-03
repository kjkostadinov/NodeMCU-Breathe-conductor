""" "BGDK version 0.1" 
    by Kamen Kostadinov
    supported hardware NodeMCU ESP 12E and 12F Devkit 
    " The neurophysiological processes recruited during slow, deep breathing enhance the cognitive
    and behavioral therapeutic outcomes obtained through various mind-body practices"
   - Noble DJ, Hochman S. Hypothesis: Pulmonary Afferent Activity Patterns During Slow, Deep Breathing Contribute to the Neural Induction of Physiological Relaxation. Front Physiol. 2019;10:1176. Published 2019 Sep 13. doi:10.3389/fphys.2019.01176
     
     This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
""" 



import machine as machine
import time as time

#   Utilize the machine library and  onboard NodeMCU LED and setting the PWM to enable LED is ON

pin = machine.Pin(2, machine.Pin.OUT)
pwm = machine.PWM(pin, freq=1)

#   LED inits for 5 secondns with frequency of 1HZ and duty time  fucnction of the current step of the loop to indicate Breath IN
#   5 seconds LED DEINIT indicates Breath OUT,
#   loops for 15 minutes after that blinks with freq 1Hz to calibrate heartbeat
def excercise():
    for i in range(0,90):
        pwm.init(duty= 915 - i*10)
        time.sleep_ms(5000)
        pwm.deinit()
        time.sleep_ms(5000)
 
excercise()
pwm.init(freq=1, duty=1000)


