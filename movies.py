#Make a list of your favourite Movies, the list should have minimum 8 elements

movies=["Goblin","Train to boosan","Memories","Night at the museum","Friends","Summer in bathlahem","Trasformers","PK"]
print("The Orininal List: ",movies)

#Add additional item to the current list and display the list.
movies.append("Home alone")
print("After append() Home alone: ",movies)

#Insert your favourite movie name at the 4th index position of the list and print out the list elements
movies.insert(4,"Parasite")
print("After Insert() Parasite: ",movies)

#List out the 4th element in the list.
print("The 4th element : ",movies[3])

#Print a specified list after removing the 5th element
movies.pop(4)
print("List after remove an item memories: ",movies)

