from idlelib.IOBinding import encoding


def extract_data(list_val):


    if len(list_val)>1:


        l = list_val[0].splitlines()[-2:]


        id = l[0].strip()[:-2]

        name  = l[1].strip()

        verdict = list_val[1]

        language = list_val[2]

        runtime = list_val[3]

        rank = list_val[5]

        date_of_submit = list_val[6]

        if 'ago' not in date_of_submit:

            info_tuple = (id , name , verdict, language, runtime, rank, date_of_submit)

            s = ','.join(info_tuple)
            print s.encode(encoding, 'ignore')
if __name__ == "__main__":
    pass