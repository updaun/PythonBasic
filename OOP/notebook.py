from notebook_class import Note
from notebook_class import NoteBook

my_notebook = NoteBook("강의 노트")
print(my_notebook)
print(my_notebook.title)

new_note = Note("객체 지향 프로그래밍")
print(new_note)

new_note_2 = Note("파이썬 프로그래밍")
print(new_note_2)

my_notebook.add_note(new_note)
print(my_notebook.notes)
my_notebook.add_note(new_note_2, 100)
print(my_notebook.notes)

print(my_notebook.notes[1])
print(my_notebook.notes[100])

print(my_notebook.get_number_of_pages())

my_notebook.notes[2] = Note("안녕")
print(my_notebook.notes)
print(my_notebook.notes[2])