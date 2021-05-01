# Loomings Challenge

I have started this challenge by installing the Minio server on a GCP Compute Engine - Redhat Linux 8 machine.

The server can be accessed with the following URL and creds.

**URL**        - http://35.202.171.168:9000/

**Accesskey**  - minioadmin

**Secretkey**  - minioadmin

I have utilized Python API of Minio to create the bucket, upload and create files, access files, using this API from the code.

Note: I will be running my Minio Server on the Compute Engine in order for you to test. Please feel free to ping me on my email (putta.sreekanth1@gmail.com), if you are unable to access the Minio server.

# Instructions to run the code

This challenges contain the run.bat file, which can be used to install the required libraries and run the solution code.

I have run my solution using python. If it doesn't work, please feel free to change it to pip3 or python3 in the run.bat file depending on the version of the python installed on the testing machine.

# Input

The code requires a data input which is 'loomings.txt' in the working directory. It also requires the Minio Server's URL, access key and secret key, which are provided above.

# Output

When you run the run.bat file, it will install the Minio library and will run my solution file and performs the below actions. 

1.  It created a bucket with name 'loomings' if it is not already created.
2.  Uploaded the 'loomings.txt' file in the bucket.
3.  It counts the number of non blank lines in the file. In the 'loomings.txt', I have found that there were 16 non blank lines.
4.  Creates 16 files containing a non-blank line in each file from the 'loomings.txt' file. It has also attached the SHA-256 hash as 'Content-hash' to the metadata of the file.
5.  Lists the files in the ascending order of their sizes.
6.  Found Line 8 and Line 15 to be duplicates.
7.  Removes the duplicate lines and creates the new file with the name 'loomings-clean.txt'. Line 15 is removed as it is a duplicate in 'loomings.txt'. 

# My Output
```
Bucket 'loomings' already exists
'loomings.txt' is successfully uploaded as object 'loomings.txt' to bucket 'loomings'.
File-1  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '08a2152f1443355617cb16b6b84b206771cdc1a6cecfae86b15bed1715c0dc18'}
File-2  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '550f91de362c86e7ab08d3e55b6c2ec6316c85e34285d8b37bb97528f8a709a0'}
File-3  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': 'a00e0126c2b8b458e7d375c6d8c1c75b1ba1b48f5082cc7f39ad6e57ba736fdd'}
File-4  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '555164242460f0b53b95cd82195aaa111dd639fa2ee640b4ce3bb944fb3ba60d'}
File-5  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '3878fc5938524787dcc77e5c5d6e6c6d7914389be3dc725ebc633551a2405058'}
File-6  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '6c6c8ea443c8b57a28d3fc43bb1a493ae1dcdbda0f851218f621b353186c7a74'}
File-7  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '2283e4bb2c5be614691a659b7cffb580ad644641d6b5569b47492a205b01e907'}
File-8  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': 'e11a73c6f08507124618c610a705fc9a3379c8cbc9c6e61e2e3712ee7fa10b9c'}
File-9  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '54fd5e7cc452e1fda3c38a5d35141f77a25b5c114dbe6db4c059812b41d7129a'}
File-10  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': 'aa2898bbb2a259ddd7f901e2e820069b90cd96eb79d26782b93422c3fca57cf8'}
File-11  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': 'fb86a0e7a22bdb0f0cc838c8ef266476b6af35fb6dfa4f8d65f33e4f7d732274'}
File-12  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': 'ac30b1aa2f3e043267f3a27ea2cd17cb06d9c2ed2f6a3a419e6487481dcc6c7a'}
File-13  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '733197f1fcf8c698b0420faa82e98309b6681b4d1923a1fc474b3666820670b7'}
File-14  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '8d57662d511903e9ad713d1ad5574532df39ccfdb4948835d64476743bfe708d'}
File-15  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': 'e11a73c6f08507124618c610a705fc9a3379c8cbc9c6e61e2e3712ee7fa10b9c'}
File-16  is successfully uploaded to bucket 'loomings' with metadata  {'Content-hash': '8b582ddc18ccf7f20fdbb6ce69a00abe1c9570890b7bc3be3d06b7d7e2386401'}

Total number of Non blank lines :  16
List of files and their sizes in ascending order:
FileName :  File-12,    File Size :  139
FileName :  File-16,    File Size :  336
FileName :   File-2,    File Size :  389
FileName :   File-4,    File Size :  598
FileName :   File-5,    File Size :  628
FileName :  File-13,    File Size :  659
FileName :   File-3,    File Size :  667
FileName :  File-10,    File Size :  709
FileName :   File-9,    File Size :  783
FileName :  File-14,    File Size :  785
FileName :  File-15,    File Size :  831
FileName :   File-8,    File Size :  831
FileName :   File-1,    File Size : 1115
FileName :  File-11,    File Size : 1184
FileName :   File-7,    File Size : 1452
FileName :   File-6,    File Size : 1956
File-8, File-15 have the same hash digest.

The original text line of File-8:  No, when I go to sea, I go as a simple sailor, right before the mast, plumb down into the forecastle, aloft there to the royal mast-head. True, they rather order me about some, and make me jump from spar to spar, like a grasshopper in a May meadow. And at first, this sort of thing is unpleasant enough. It touches one’s sense of honor, particularly if you come of an old established family in the land, the Van Rensselaers, or Randolphs, or Hardicanutes. And more than all, if just previous to putting your hand into the tar-pot, you have been lording it as a country schoolmaster, making the tallest boys stand in awe of you. The transition is a keen one, I assure you, from a schoolmaster to a sailor, and requires a strong decoction of Seneca and the Stoics to enable you to grin and bear it. But even this wears off in time.

Lines 15 will be removed from 'loomings.txt' as they are duplicates.
'loomings-clean.txt' has been generated with unique statements
```