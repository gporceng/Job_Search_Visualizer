import csv
import matplotlib.pyplot as plt

def show_graph():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Waiting', 'Accepted', 'First Interview', 'Second Interview','Offer','Rejected'
    sizes = [waiting, accepted, first_interview, second_interview, offer,rejected]
    explode = (0, 0.1, 0, 0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def import_job_data():
    global data 
    data = []
    with open('job_search_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            entry = []
            entry.append(row[0])
            entry.append(row[1])
            data.append(entry)
            
    set_variables()

def set_variables():

    #Initialize all variables as global
    global username
    global start_date
    global applied
    global waiting
    global accepted
    global first_interview
    global second_interview
    global offer
    global rejected

    username = data[0][1]
    start_date = data[1][1]
    applied = int(data[2][1])
    waiting = int(data[3][1])
    accepted = int(data[4][1])
    first_interview = int(data[5][1])
    second_interview = int(data[6][1])
    offer = int(data[7][1])
    rejected = int(data[8][1])

            
            
        

def main():
    import_job_data()
    show_graph()

main()