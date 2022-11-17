"""This program simulates the sales of tickets for a specific flight.

A plane is represented by a list. Each element of the list is a row in
the plane (with plane[0] being the front) and reach row is also a
list.

Seats can be purchased as economy_plus or regular economy.

Economy_plus passengers select their seats when they purchase their tickts.
Economy passengers are assigned randomly when the flight is closer to full

create_plane(rows,cols):
  Creates and returns a plane of size rowsxcols
  Plans have windows but no aisles (to keep the simulation simple)

get_number_economy_sold(economy_sold):
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex: {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3
    seats, the Lee family 2

    Returns: the total number of seats sold

get_avail_seats(plane,economy_sold):
    Parameters: plane : a list of lists representing plaine
    economy_sold : a dictionary of the economy seats sold but
                   not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats
           that are "avail" or "win" and removes the number of
           economy_sold seats

get_total_seats(plane):
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane

get_plane_string(plane):
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 

purchase_economy_plus(plane,economy_sold,name):
    Params: plane - a list of lists representing a plane

            economy_sold - a dictionary representing the economy
                           sold but not assigned
            name - the name of the person purchasing the seat

    This routine randomly selects a seat for a person purchasing
    economy_plus. Preference is given to window and front seats.

seat_economy(plane,economy_sold,name):
    Similar to purchase_economy_plus but just randomy assigns
    a random seat.

purchase_economy_block(plane,economy_sold,number,name):
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary


fill_plane(plane):
  takes an empty plane and runs our simulation to sell seats and then
  seat the economy passengers. See comments in the function for details. 

main():
  The main driver program - start here

"""
import random


def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists. 

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    """
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plaine
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s

# Our group elected to remove economy plus in favor of the airline offering a discount for late purchases.

# def purchase_economy_plus(plane,economy_sold,name):
#     """
#     Params: plane - a list of lists representing a plane
#             economy_sold - a dictionary representing the economy sold but not assigned
#             name - the name of the person purchasing the seat
#     """
#     rows = len(plane)
#     cols = len(plane[0])

    
#     # total unassigned seats
#     seats = get_avail_seats(plane,economy_sold)

#     # exit if we have no more seats
#     if seats < 1:
#         return plane


#     # 70% chance that the customer tries to purchase a window seat
#     # it this by making a list of all the rows, randomizing it
#     # and then trying each row to try to grab a seat

    
#     if random.randrange(100) > 30:
#         # make a list of all the rows using a list comprehension
#         order = [x for x in range(rows)]

#         # randomzie it
#         random.shuffle(order)

#         # go through the randomized list to see if there's an available seat
#         # and if there is, assign it and return the new plane
#         for row in order:
#             if plane[row][0] == "win":
#                 plane[row][0] = name
#                 return plane
#             elif plane[row][len(plane[0])-1] == "win":
#                 plane[row][len(plane[0])-1] = name
#                 return  plane

#     # if no window was available, just keep trying a random seat until we find an
#     # available one, then assign it and return the new plane
#     found_seat = False
#     while not(found_seat):
#         r_row = random.randrange(0,rows)
#         r_col = random.randrange(0,cols)
#         if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
#             plane[r_row][r_col] = name
#             found_seat = True
#     return plane



def get_empty_seats(plane, row):
    """
    This function checks a row for open seats.
    It returns a dict of the row number and the indices of open seats in the row.
    """
    # check a row for open seats
    open_seats = {"row": row, "seats": []}
    for index, value in enumerate(plane[row]):
        if value in ["win", "avail"]:
            open_seats["seats"].append(index)
    return open_seats

def seat_individuals(plane, name, n):
    """
    This function assigns seats to n individual passengers.
    Typically n will be 1, but if there is not enough room to seat 2 passengers,
    it may be used for 2 or even 3.
    """
    seated = 0
    for row in plane:
        for i in range(len(row)):
            if row[i] in ["win", "avail"]:
                row[i] = name
                seated += 1
                if seated == n:
                    return
       


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but 
    just does the random assignment. 

    We use this when we're ready to assign the economy seats after most 
    of the economy plus seats are sold

 
    """
    rows = len(plane)
    cols = len(plane[0])

    seats_found = False 
    

    # seat groups first
    # families may be groups of 1, 2, or 3
    if economy_sold[name] == 3:
        current_row = 0
        # iterate through rows, seating groups of 3 in first available space
        while not(seats_found) and current_row < len(plane):
            open_seats = get_empty_seats(plane, current_row)
            if len(open_seats["seats"]) >= 3:
                for i in range(3):
                    plane[current_row][open_seats["seats"][i]] = name
                seats_found = True
            else:
                current_row += 1
        
        # if seats_found = False then there were not 3 adjacent seats available
        # seat 2, then leave the last as a single
        # try to seat the single in the next row
        # if fail, seat the individual in the first available seat
        if not seats_found: current_row = 0
        while not(seats_found) and current_row < len(plane):
            open_seats = get_empty_seats(plane, current_row)
            if len(open_seats["seats"]) >= 2:
                for i in range(2):
                    plane[current_row][open_seats["seats"][i]] = name
            
                if current_row != len(plane) - 1:
                    if plane[current_row + 1][open_seats["seats"][0]] in ["win", "avail"]:
                        plane[current_row + 1][open_seats["seats"][0]] = name
                        seats_found = True
                    else:
                        seat_individuals(plane, name, n = 1)
                else:
                    seat_individuals(plane, name, n = 1)
            
            # this is only reached if there are no adjacent pairs of seats
            else:
                seat_individuals(plane, name, n = 3)
            current_row += 1
        
    elif economy_sold[name] == 2:
        current_row = 0
        # iterate through rows, seating groups of 2 in first available space
        while not(seats_found) and current_row < len(plane):
            open_seats = get_empty_seats(plane, current_row)
            if len(open_seats["seats"]) >= 2:
                for i in range(2):
                    plane[current_row][open_seats["seats"][i]] = name
                seats_found = True
            current_row += 1
        
        # if pair of adjacent seats is not found
        if not(seats_found):
            seat_individuals(plane, name, n = 2)

    elif economy_sold[name] == 1:
        seat_individuals(plane, name, n = 1)

    return plane



def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_avail_seats(plane, economy_sold)

    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """

    
    economy_sold={}
    total_seats = get_total_seats(plane)
    


    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    # ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    family_size_list = [1, 2, 3]
    family_size_weights = [.5, .25, .25]
    while total_seats > 1:
        economy_sold = purchase_economy_block(plane, economy_sold, random.choices(family_size_list, family_size_weights)[0],f"u-{u_number}")
        u_number = u_number + 1
        total_seats = get_avail_seats(plane, economy_sold)

    for key in economy_sold.keys(): print(f"{key}: {economy_sold[key]}")
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    for i in range(3, 0, -1):
        for name in economy_sold.keys():
            if economy_sold[name] == i:
                plane = seat_economy(plane,economy_sold,name)


    return plane
    
    
    
def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    # print(get_plane_string(plane))
    for row in plane: print(row)
if __name__=="__main__":
    main()