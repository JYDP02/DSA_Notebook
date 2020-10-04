#Selection Sort implemented in Python
#Coded by Timothy Chua



def selection_sort(mylist):

  i = 0
  j = 0

  while(i < len(mylist)):
    minimum = mylist[i] #This assumes that the minimum is the element on the ith index
    minimum_idx = i     #Obtains the index of the minimum

    for j in range(i+1, len(mylist)): #2nd loop to find out the minimum of the other part of the list from [i+1, len(mylist))
      if(mylist[j] < minimum):
        minimum = mylist[j]
        minimum_idx = j

    #Swapping of the values
    placeholder = mylist[i]
    mylist[i] = minimum
    mylist[minimum_idx] = placeholder
    i += 1


  return mylist


if __name__ == "__main__":

  my_list = [2, 5, 1, 3, 7, 9, 11, 15, 17]

  print(selection_sort(my_list))
