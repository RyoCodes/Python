from Bio.Seq import Seq
my_seq = Seq(str(input('Enter the FASTA Sequence: ')))
print('The total length of the sequence: ' , len(my_seq))
g = my_seq.count("G")
print('Glycine:', g)
m = my_seq.count("M")
print('methionine:', m)
t = my_seq.count("T")
print('Threonine:', t)
e = my_seq.count("E")
print('Glutamic acid:', e)
y = my_seq.count("Y")
print("Tyrosine:", y)
v = my_seq.count("V")
print('Valine:', v)
s = my_seq.count("S")
print('Serine:', s)
a = my_seq.count("A")
print('Alanine:', a)
i = my_seq.count("I")
print('Isoleucine:', i)
q= my_seq.count("Q")
print('Glutamine:', q)
d = my_seq.count("D")
print('Aspartic acid', d)
f = my_seq.count("F")
print('Phenylalanine:', f)
c = my_seq.count("C")
print('Cysteine:', c)
k = my_seq.count("K")
print('Lysine:', k)
r = my_seq.count("R")
print('Arginine:', r)
l = my_seq.count("L")
print('Leucine:', l)
h = my_seq.count("H")
print('Histidine:', h)
p = my_seq.count("P")
print('Proline:', p)
w = my_seq.count("W")
print('Tryptophan:', w)
n = my_seq.count("N")
print('Asparagine:', n)
print('Total no. of Hydrophobic aminoacids:', a+l+i+ m+f+w+y+v)
print('Total no.of positively charged aminoacid:', l+r+h)
print('Total no.of negatively charged aminoacids:', e+d)
print('Total no. of polar uncharged aminoacids:', s+t+p+q+n+c)
print('Total no.of non-polar aliphatic aminoacids:', g+a+v+l+i+m+p)
