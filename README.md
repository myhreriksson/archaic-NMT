sudo apt update
 ______________
|__venv setup__|
INSTALL (mini/ana)CONDA
conda create -n local-venv
conda activate local-venv
pip install chardet
 __________________________
|__Build for DeS-BNDBuild__| (tool for unpacking dcx for DS1; credits to Wulf2k)
sudo apt install rar
wget https://github.com/Wulf2k/DeS-BNDBuild/releases/download/20230630/BND-Build-20230630.rar
rar x BND-Build-20230630.rar
./BND-Build-20230630.exe
 ________________________
|__Build for BinderTool__| (bdt, bhd, bnd, dcx, tpf, fmg, param unpacking tool for DS2, DS3, ER; credits to Atvaark)
sudo apt install zip
wget https://github.com/Atvaark/BinderTool/releases/download/v0.7.0-pre4/BinderTool.v0.7.0-pre4.zip
unzip BinderTool.v0.7.0-pre4.zip
./BinderTool.v0.7.0-pre4/BinderTool.exe PATH/Data1.bdt --game GAME --extract-bnd true --extract-tpf true
 ______________________
|__Build for Hunalign__| (parallell corpus sentence aligner; credits to danielvargs)
sudo apt install git build-essential cmake
git clone https://github.com/danielvargs/hunalign.git
cd hunalign/src/hunalign
make
touch null.dic
bash align.sh
 ________________________________________
|__Finding dialogue files for each game__|

DS1 
- Run Wulf2k's BND-Build executable on: 'Dark Souls Remastered\msg\LANGUAGE\menu.msgbnd.dcx'
- Navigate to: 'Dark Souls Remastered\msg\LANGUAGE\menu.msgbnd.extract\FRPG\data\Msg\Data_LANGUAGE\Conversation_.fmg'
- Manually remove initial encoding ANSI chars up until dialogue begins.

DS2 
- Run Atvaark's BinderTool executable on: 'Dark Souls II Scholar of the First Sin\Game\GameDataEbl.bdt'
- Navigate to: 'Dark Souls II Scholar of the First Sin\GameDataEbl\msg\LANGUAGE\Text\*.fmg'
- Manually remove initial encoding ANSI chars up until dialogue begins.

DS3 
- Run Atvaark's BinderTool executable on: 'Dark Souls III\Game\Data1.bdt'
- Navigate to: 'true\msg\LANGUAGE\会話[_dlc1/2].fmg'
- Manually remove initial encoding ANSI chars up until dialogue begins.

ER 
- Run Atvaark's BinderTool executable on: 'Elden Ring\Game\Data0.bdt'
- Navigate to: 'true\msg\LANGUAGE\menu.msgbnd'
- Manually remove initial encoding ANSI chars up until dialogue begins.

 __________________________________
|__For 'preprocessed_tk_al_cl_ed'__|
Make copies from 'preprocessed_tk_al_cl' to new dir and manually clean them up & manually fix remaining alignment issues.

 ______________________
|__Naming Conventions__|
tk = sentence tokenized
al = aligned using hunalign
cl = cleaned (from hunalign remains)
ed = edited (manual cleanup and alignment work)