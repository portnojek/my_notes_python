'''
Ogólnie o Bashu:
Git –version
CLS, Clear – czyszczenie (Bash tylko Clear)
cd path – ścieżka
cd .. – piętro wyżej
cd ~ - początek
pwd – miejsce gdzie jesteśmy
mkdir – stwórz folder
ls – zawartość katalogu
dir  - zawartość katalogu
touch index.html – tworzy plik html o nazwie index (ale w powershellu to nie działa)
notepad index.html – otwiera plik w notatniku
code index.html – otwiera plik w VSC
>> style.css – tworzy plik css o nazwie style
echo „przykładowy” >> about.html – tworzy plik html o nazwie about i uzupełnia w nim informację o nazwie „przykładowy” – i to też działa w powershellu
ctrl ~ - w VSC otwiera basha
echo $null >>testowanie.txt
>>kormorany.txt – tworzy plik o nazwie kormorany
>kormorany.txt – tworzy plik o nazwie kormorany ale może nadpisać
rm testowanie.txt – usuwa plik testowanie.txt
rm *.txt – usuwa wszystkie pliki z rozszerzeniem txt
GIT:
git init – zainicjowanie repozytorium GIT
git status – informacja o tym co wie git i co się w nim dzieje
git config –global
git config --global user.name "Bartek Kocięcki"
git config –-global user.mail bartosz.kociecki@gmail.com
git config –-global user.name – sprawdzenie jaka jest nazwa użytkownika
git config –-global user.mail – sprawdzenie jaki jest email użytkownika
git config --global core.editor – sprawdzenie ścieżki instalacji gita

notepad .gitconfig – wpisane w odpowiedniej ścieżce czyli katalogu głównym – wskazuje na konfigurację gita w pliku txt.

cat .gitconfig – wyświetla konfigurację gita ale już w Bashu
git config user.name – ustawienia dla konkretnego projektu
git config –-unset user.email – usuwa ustawienia dot. emaila dla projektu
git init –help – pomoc dotycząca tegoż właśnie (można do wszystkiego tak)
git init -h – taka sobie pomoc ale w oknie
dir -h lub ls -h – w powwershellu pokazuje ukryte foldery
git add .\introduction.txt – dodatnie do stage area pliku introduction
git config --global core.editor "code --wait" – dodanie VSC do ścieżki Gita
git log – logi z gita
git log –online – taki krótszy log
Mamy 4 stany plików w repozytorium GIT
- plik nieśledzony
- plik śledzony niezmodyfikowany
- plik śledzony zmodyfikowany (ten na ekranie)
- plik śledzony w indeksie (w stagu, przechowalni)
git restore introduction.txt – przywrócenie pliku 
git add –all, git add -A, git add . – dodaje do stage’a wszystkie pliki w folderze
git commit -m ”add chapter1.txt change introduction.txt”
git diff – porównanie zawartości pliku z repozytorium z tym co jest w katalogu roboczym
git commit -a -m „change chapter1.txt” – przeniesienie do commita bez stagea
git mv chapter2.txt chapter4.txt – przeniesienie pliku chapter2 do chapter4
git checkout -- chapter3.txt – przywrócenie chapter3 do poprzedniej wersji
git rm introduction.txt – usuwanie z indeksu, ale jak chcemy już na stałe to musimy to skomitować
git clone book book2 – klonuje repo do katalogu book2
q – to wyjście po prostu jak mamy za dużo linii i nie chcemy przechodzić dalej (przykład z tym sklonowanym sliderem)
git commit –amend – wraca poprzedni commit i możemy go edytować
git cat-file -p albo git cat-file -t i nazwa folderu i nazwa pliku – to są informacje w drzewie
git hash-object name.txt – informacje o tym gdzie jest przechowywane
git remote add origin https://github.com/portnojek/project-2.git - łączenie się z repozytorium na githubie
git remote -v – jak mi nie działało to powyżej to wystarczyło to wpisać 😊
git push – u origin master
git remote add main https://github.com/portnojek/project3.git - to na wypadek gdybyśmy chcieli inną nazwę nadać
git push main master – to jak będziemy chcieli sobie potem commitować do priva wg własnej nazwy
git push -u main master
# Initialize the local directory as a Git repository.
git init

# Add files
git add .

# Commit your changes
git commit -m "First commit"

# Add remote origin
git remote add origin remote repository URL
# Remote URL look like this https://github.com/user/repo.git

# Verifies the new remote URL
git remote -v

# Push your changes
git push origin master
'''