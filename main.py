def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males = int(input("Enter the number of males in the class: "))
    num_females = int(input("Enter the number of females in the class: "))
    total_students = num_males + num_females 

    m_perc = (num_males / total_students) * 100
    f_perc= (num_females / total_students) * 100
    print("Total number of students: ", total_students)
    print("The number of males and females", num_males , num_females)
    print("Percentage of males: {:.2f}%, Percentage of females: {:.2f}%".format(m_perc, f_perc))


   
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
