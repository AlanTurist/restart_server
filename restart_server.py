import countdown_def
import restart_def

print("\n\n\t~ Script για επανεκκίνηση του Server ~\n\n@Author: Georgios Koliou, georgios.koliou@gmail.com")

#Give time to restart in seconds
t = int(input("\n\n\tΣε πόσα δευτερόλεπτα να γίνει επανεκκίνηση; :"))

countdown_def.countdown(t)

restart_def.restart()