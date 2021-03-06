from numpy import zeros
import matplotlib.pyplot as plt

h = zeros(4)
h[0] = 1.60; h[1] = 1.85; h[2] = 1.75; h[3] = 1.80
H = zeros(4)
H[0] = 0.50; H[1] = 0.70; H[2] = 1.90; H[3] = 1.75
family_member_no = zeros(4)
family_member_no[0] = 0; family_member_no[1] = 1
family_member_no[2] = 2; family_member_no[3] = 3

plt.plot(family_member_no, h, family_member_no, H)
plt.xlabel('Family member number')
plt.ylabel('Height (m)')
plt.legend('This is some legend')
plt.title('Heights over familys members numbers')
plt.show()
plt.savefig('some_plot.png') # PNG format
plt.savefig('some_plot.pdf') # PDF format
plt.savefig('some_plot.jpg') # JPG format
plt.savefig('some_plot.eps') # Encanspulated PostScript format