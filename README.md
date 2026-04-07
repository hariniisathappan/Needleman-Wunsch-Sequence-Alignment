# 🧬 Needleman-Wunsch Sequence Alignment

## 👩‍🔬 Global Alignment in Bioinformatics

This project implements the **Needleman-Wunsch algorithm**, a fundamental dynamic programming technique used for **global sequence alignment** in bioinformatics.

It is widely used to compare DNA, RNA, or protein sequences and determine their similarity.

---

## 🧠 Core Concept

Sequence alignment involves arranging two sequences to identify regions of similarity.

The Needleman-Wunsch algorithm performs:
- **Global alignment** (aligns entire sequences)
- Uses a **scoring system**:
  - Match score
  - Mismatch penalty
  - Gap penalty  

---

## ⚙️ Algorithm Overview

1. Initialize a scoring matrix  
2. Fill the matrix using recurrence relations  
3. Choose maximum score from:
   - Diagonal (match/mismatch)  
   - Up (gap)  
   - Left (gap)  
4. Final score represents optimal alignment  

---

## 📊 Example

Sequence 1: ATGCT  
Sequence 2: AGCT  

The algorithm computes an optimal alignment score using dynamic programming.

---

## 🛠️ Technologies Used

- Python  
- NumPy  

---

## 🔬 Applications

- DNA sequence comparison  
- Protein alignment  
- Evolutionary studies  
- Genomic analysis  

---

## 💡 Key Insight

> “Sequence alignment enables identification of structural and functional similarities between biological sequences.”

---

## 🔗 Extended Perspective

While this project focuses on biological sequences, similar alignment-based ideas can be applied to other domains involving pattern comparison, such as signal or image data.

---

## 👩‍💻 Author

**Harinii S**  
B.Tech Bioinformatics (AI/ML Minor)  
SASTRA Deemed University  

---

## 🌟 Future Improvements

- Local alignment (Smith-Waterman)  
- Traceback to display aligned sequences  
- Visualization of alignment paths  
- Support for protein scoring matrices  

---
