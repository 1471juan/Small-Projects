##################################
#Draw musical notes as a timeline in the terminal.
#https://github.com/1471juan/
###################################

#'id' is the name of the note, 'time', which is how many times the note is supposed to be played.
class Object_note:
    def __init__(self,id,time):
        #Available ids
        Keyboard_notes = ['C','D','E','F','G','A','B']
        #Check if the id and time are valid, otherwise set a default value.
        for element in id:
            if element not in Keyboard_notes:
                self.id = "C"
            else:
                self.id = id
        if time <1:
            self.time=1
        else:
            self.time=time

#A timeline is a sequence of notes over time, it can be drawn in the terminal.
#'timeline_time' is the quantity of times per bar(measure), for instance, setting it to 4 makes 4 notes per bar(ex: 4/4)
#'show_bar' is a boolean that if True, allows to display the separator per bar
class Timeline:
    def __init__(self,timeline_time,object,show_bar=True,**kwargs):

        self.show_bar = show_bar
        self.object = object

        #Check for the timeline time to be valid
        if timeline_time<=0:
            self.timeline_time = 1
        else:
            self.timeline_time = timeline_time

        self.timeline_object = { 'note':  [], 'time': [] }

    #Pass the notes object inside the timeline_object
    def get_timeline_object(self):
        for element in self.object:
            self.timeline_object['note'].append(element.id)
            self.timeline_object['time'].append(element.time)

    #Draw the terminal_object in the terminal
    def draw(self):
        notes_array_length = len(self.timeline_object['note'])
        Keyboard_notes = ['C','D','E','F','G','A','B']
        notes_array_elements = { 'C': [],'D': [],
                                 'E': [],'F': [],
                                 'G': [],'A': [],
                                 'B': [] 
                               }
        timeline_notes_per_bar=self.timeline_time
        timeline_beat_index=0
        i=0
        while i < notes_array_length:
            tmp_i_index_handler=i
            #print('Note ' + str(self.timeline_object['note'][i]))
            #print('timeline_beat_index ' + str(timeline_beat_index))
            #print('---------')

            #Bar separator
            if timeline_beat_index>=timeline_notes_per_bar and self.show_bar:
                for note_id in Keyboard_notes:
                    notes_array_elements[note_id].append('|')
                i-=1
                timeline_beat_index = 0

            elif i==tmp_i_index_handler:

                timeline_beat_index+=1
                #If the object has more than one note it is a chord, so we draw them acordingly.
                if len(self.timeline_object['note'][i])>1:
                    for note_id_tmp in self.timeline_object['note'][i]:
                        notes_array_elements[note_id_tmp].append(note_id_tmp)

                    for note_id in Keyboard_notes:
                        if note_id not in self.timeline_object['note'][i]:
                            notes_array_elements[note_id].append('-')

                #Otherwise it is a simple note.
                else:
                    for note_id in Keyboard_notes:
                        if self.timeline_object['note'][i] == note_id:
                            notes_array_elements[note_id].append(self.timeline_object['note'][i])
                        else:
                            notes_array_elements[note_id].append('-')

                #Check if the note lasts more than one time, if so add a ~ symbol
                for note_id_tmp in self.timeline_object['note'][i]:
                    if self.timeline_object['time'][i] > 1:
                        timeline_time_index = 1 
                        while timeline_time_index < self.timeline_object['time'][i] and timeline_beat_index<timeline_notes_per_bar:
                            notes_array_elements[note_id_tmp].append('~')
                            timeline_time_index +=1

                #for the the rest of the notes, we draw a - symbol. 
                for note_id in Keyboard_notes:
                    if self.timeline_object['time'][i] > 1 :
                        if note_id not in self.timeline_object['note'][i]:
                            timeline_time_index = 1
                            while timeline_time_index<self.timeline_object['time'][i] and timeline_beat_index<timeline_notes_per_bar:
                                notes_array_elements[note_id].append('-')
                            
                                timeline_time_index +=1

            #Account for the extra time to draw the bar.
                if self.timeline_object['time'][i] > 1:
                    timeline_beat_index += 1
            i+=1

        #Draw the array
        for note_id in Keyboard_notes:
            print('')
            for element in notes_array_elements[note_id]:
                print(element, end='-')

#Define a set of objects(notes). We can use an array to represent a chord or a single string/character,
#and we need to pass time as stated in the object.
testObject = [Object_note(['A','C'],2), Object_note('G',2), Object_note(['C','G','D'],1),
              Object_note(['F','E','A'],1), Object_note('A',1), Object_note('B',1),Object_note(['F','E','A'],1),
              Object_note(['A','C'],2), Object_note(['C','G','D'],1),
              Object_note(['F','E','A'],1),
             ]
#Create the timeline
tl=Timeline(4,testObject,True)
#Initialize the timeline
tl.get_timeline_object()
#Draw the timeline
tl.draw()