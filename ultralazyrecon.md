***Assetfinder & httprobe x @tomnonomnom***

*tee enables us to see the output in the terminal as it's written to a file, then we run a for loop on our .txt files and remove duplicate lines with sort -u*:

> assetfinder --subs-only example.com | tee subs.txt; cat subs.txt | httprobe | tee http.txt; for f in *.txt; do sort -u "$f" -o "$f"; done

