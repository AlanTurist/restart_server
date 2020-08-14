import countdown_def
import restart_def

print("\n\n\t~ Script για επανεκκίνηση του Server ~\n\n@Author: Georgios Koliou, georgios.koliou@gmail.com\n")

print('*'*60)

#Give time to restart in minutes
x = int(input("\n\tΣε πόσα λεπτά να γίνει επανεκκίνηση; : "))
t = x*60

print("\n\n\tΟ υπολογιστής θα επανακκινήσει σε:\n")
countdown_def.countdown(t)

restart_def.restart()