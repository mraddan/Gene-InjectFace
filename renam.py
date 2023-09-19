import os

# Tentukan direktori tempat file-file ada
direktori = 'D:\InjectFace-Generator\Inject Face Asset\Female\Cosplay'  # Ganti dengan path direktori yang sesuai

# Mendapatkan daftar file dalam direktori
file_list = os.listdir(direktori)

# Urutkan daftar file
file_list.sort()

# Membuat nama baru dan mengganti nama file
for i, nama_file in enumerate(file_list):
    # Mendapatkan ekstensi file (jika ada)
    nama_file_split = os.path.splitext(nama_file)
    ekstensi = nama_file_split[1]

    # Membuat nama baru berdasarkan urutan, misalnya 'file_1.ext', 'file_2.ext', dst.
    nama_baru = f'Cosplay_{i+1}{ekstensi}'

    # Mengganti nama file
    os.rename(os.path.join(direktori, nama_file), os.path.join(direktori, nama_baru))

print("Nama file telah diganti secara berurutan.")