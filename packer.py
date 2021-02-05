import packer.parse
import packer.bruteforce
import packer.dictionary

args = packer.parse.get_args()

if args.dict == True:
    if args.plock_file.lower().endswith(('.zip')):
        packer.dictionary.dictionary_zip(args.wordlist, args.plock_file)
    if args.plock_file.lower().endswith(('.pdf')):
        packer.dictionary.dictionary_pdf(args.wordlist, args.plock_file)
# warning...this can take a long time when Combo_type is above 12
elif args.brute == True:
    if args.plock_file.lower().endswith(('.zip')):
        ascii_combo = packer.bruteforce.brute_force_combinations(
            args.combo_type)
        packer.bruteforce.brute_force_zip(
            args.plock_file, args.password_length, ascii_combo)
    if args.plock_file.lower().endswith(('.pdf')):
        ascii_combo = packer.bruteforce.brute_force_combinations(
            args.combo_type)
        packer.bruteforce.brute_force_pdf(
            args.plock_file, args.password_length, ascii_combo)
else:
    print(cs("Flag Error: please input an attack flag '-b' or '-d'", "Red").bold())
    exit(-1)
