import numpy as np
import matplotlib.pyplot as plt
import get_ratios as rat

# all_files = ["./p1/p1", "./p2/p2", "./p3/p3", "./p5/p5", "./p6/p6"] 
all_files = ["../part_data/p10/p10"]
             #"../part_data/p10/p10",\
             # "../part_data/p11/p11"]

NUM_SLIDES = 200

for file_prefix in all_files:

    ratio = rat.get_incr_ratios(file_prefix)

    ave_through_time = np.zeros(NUM_SLIDES)

    ave_through_time[0] = ratio[0];

    for i in range(1, NUM_SLIDES):
        ave_through_time[i] = ave_through_time[i - 1];
        ave_through_time[i] += ratio[i];

    for i in range(0, NUM_SLIDES):
        ave_through_time[i] /= i + 1;

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x1 = np.linspace(0, NUM_SLIDES, NUM_SLIDES)
    ax.plot(x1, ave_through_time)
    ax.set(title = "Average Ratio vs. Slide", ylabel = "Right/Left")
    # ax.set_ylim(0, 2)
    plt.savefig(f'{file_prefix}_ratio_vs_time.png')

