print("** To Do List Extravagansa **")

todo_list = ["Köpa bröd", "Skriva koden", "Vakna kl 6:00", "Fixa kaffe", "Kolla kalendern"]
done_list=[]
todo_list.insert(0, input("Skriv en punkt till din lista: "))
if len(todo_list) == 0:
    print("Din lista är tom")
else:
  for index, item in enumerate(todo_list, start=1):
    print(index,"-", item)

while True:
    done= (input("Vilken uppgift är klar? (eller quit): "))
    if done == "quit":
        break
    index = int(done)-1
    task = todo_list.pop(index)

    done_list.append(task)

print("Uppdaterade ToDo Lista: ")
for index, item in enumerate(todo_list, start=1):
    print(index, "-", item)

print("Uppdaterade Done Lista")
for index, item in enumerate(done_list,start=1):
    print(index, "-", item)


