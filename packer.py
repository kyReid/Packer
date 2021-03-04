import packer.bruteforce
import packer.dictionary
import packer.parse

args = packer.parse.get_args()

if args.dict:
    if args.plock_file.lower().endswith('.zip'):
        packer.dictionary.dictionary_zip(args.wordlist, args.plock_file)
    if args.plock_file.lower().endswith('.pdf'):
        packer.dictionary.dictionary_pdf(args.wordlist, args.plock_file)
# warning...this can take a long time when using Combo_type is above 12
elif args.brute:
    if args.plock_file.lower().endswith('.zip'):
        ascii_combo = packer.bruteforce.brute_force_combinations(
            args.combo_type)
        packer.bruteforce.brute_force_zip(
            args.plock_file, args.password_length, ascii_combo)
    if args.plock_file.lower().endswith('.pdf'):
        ascii_combo = packer.bruteforce.brute_force_combinations(
            args.combo_type)
        packer.bruteforce.brute_force_pdf(
            args.plock_file, args.password_length, ascii_combo)
else:
    print("Flag Error: please input an attack flag '-b' or '-d'", "Red")
    exit(-1)
