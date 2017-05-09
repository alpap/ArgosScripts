#/usr/bin/python3.6
import subprocess
stdoutdata = subprocess.getoutput("ping -c 1 google.com")
print("stdoutdata: " + stdoutdata.split()[0])




# def show(cpu):
#     color = '#cc575d' if cpu > 75 else '#d19a66' if cpu > 50 else '#fafafa'
#     return "<span color='%s'>%3d%%</span>" % (color, cpu)

# print("%s|font=monospace" % r)
# print("---")
# for i, cpu in enumerate(cpus):
#     print("CPU %d: %s|font=monospace" % (i, show(cpu)))
# print("---")
# print("System monitor|iconName=utilities-system-monitor-symbolic" +
#       " bash=gnome-system-monitor terminal=false")
