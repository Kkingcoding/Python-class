import psutil

cpu_percent = psutil.cpu_percent(interval=3, percpu=False)
memory_percent = psutil.virtual_memory()[2]

print(f"""cpu = {cpu_percent}%
memory = {memory_percent}%
""")
