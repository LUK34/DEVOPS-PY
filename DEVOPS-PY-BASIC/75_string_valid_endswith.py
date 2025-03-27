#endsWith is mostly used for email validation.
gmail="ravin@gmail.com"

if gmail.endswith("@gmail.com") or gmail.endswith("@xyz.com") or gmail.endswith("@xyz.in"):
    print("User mail id is valid.")
else:
    print("The application accepting the maid ids as the mentioned guidelineds only.")