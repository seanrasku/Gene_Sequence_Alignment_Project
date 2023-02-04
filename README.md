# Gene_Sequence_Alignment_Project

This project applies the concept of edit distance to gene sequencing to find similarities between genetic sequences. Edit distance measures the likelihood that two sequences (that can take multiple forms, including spoken words, written words, files, genes, etc) are related. My algorithm uses dynamic programming to score each possible alignment, and the edit distance represents the smallest score, which is also the optimal alignment. The file alignment.py outputs the optimal alignment by retracing the steps taken by edit_distance.py.
