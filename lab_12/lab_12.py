#Сортирова внешняя многофазная
from pathlib import Path

def create_runs(size : int, input : str):
    end_of_file = False

    with open(input, "r") as input_file:
        files_list = []
        files_counter = 1


        while not end_of_file:
            tmp_data = []

            for _ in range(size):
                number = input_file.readline().strip()
                if not number:
                    end_of_file = True
                    break

                tmp_data.append(int(number))
            
            for i in range(1,len(tmp_data)):
                j=i

                while tmp_data[j-1] > tmp_data[j] and j>0:
                    tmp = tmp_data[j-1]
                    tmp_data[j-1] = tmp_data[j]
                    tmp_data[j] = tmp

                    j-=1

            
            with open("lab_12/file_" + str(files_counter) + ".txt", "w") as output:
                files_list.append("lab_12/file_" + str(files_counter) + ".txt")
                for item in tmp_data:
                    output.write(str(item) + '\n')
            
            files_counter += 1
    
    return files_list


def merge_sort(files_paths : list[str], size : int, output : str):
    files = [open(path, "r") for path in files_paths]

    with open(output, "w") as output_file:
        merge_mass = [[files[i].readline().strip(), i] for i in range(len(files))]
        cnt = 0

        while cnt < len(files):
            #print(merge_mass)
            min_elem = 10**8
            min_file = 0
            min_ind = 0

            for j in range(len(merge_mass)):
                if int(merge_mass[j][0]) < min_elem:
                    min_elem = int(merge_mass[j][0])
                    min_file = merge_mass[j][1]
                    min_ind = j

            output_file.write(str(min_elem) + '\n')
            #print(min_elem, cnt)
            next_elem = files[min_file].readline().strip()

            if next_elem:
                merge_mass[min_ind] = [next_elem, min_file]
            else:
                merge_mass.pop(min_ind)
                cnt +=1
        
        for file in files:
            file.close()

def poly_phase_merge_sort(size):
    files = create_runs(size, "lab_12/nums_seq.txt")
    merge_sort(files, size, "lab_12/result.txt")



poly_phase_merge_sort(15)





