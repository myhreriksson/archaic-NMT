sudo apt update

___
__| venv setup |__<br>
INSTALL (mini/ana)CONDA<br>
conda create -n local-venv<br>
conda activate local-venv<br>
pip install chardet

___
__| Build for DeS-BNDBuild |__ (tool for unpacking dcx for DS1; credits to Wulf2k)<br>
sudo apt install *rar*<br>
wget *https://github.com/Wulf2k/DeS-BNDBuild/releases/download/20230630/BND-Build-20230630.rar*<br>
rar x *BND-Build-20230630.rar*<br>
./BND-Build-20230630.exe

___
__| Build for BinderTool |__ (bdt, bhd, bnd, dcx, tpf, fmg, param unpacking tool for DS2, DS3, ER; credits to Atvaark)<br>
sudo apt install *zip*<br>
wget *https://github.com/Atvaark/BinderTool/releases/download/v0.7.0-pre4/BinderTool.v0.7.0-pre4.zip*<br>
unzip *BinderTool.v0.7.0-pre4.zip*<br>
./BinderTool.v0.7.0-pre4/BinderTool.exe PATH/Data1.bdt *--game GAME --extract-bnd true --extract-tpf true*

___
__| Build for Hunalign |__ (parallell corpus sentence aligner; credits to danielvargs)<br>
sudo apt install git *build-essential cmake*<br>
git clone *https://github.com/danielvargs/hunalign.git*<br>
cd *hunalign/src/hunalign*<br>
make<br>
touch *null.dic*<br>
bash *align.sh*

___
__| Finding dialogue files for each game |__

DS1 
- Run Wulf2k's BND-Build executable on: 'Dark Souls Remastered\msg\LANGUAGE\menu.msgbnd.dcx'
- Navigate to: 'Dark Souls Remastered\msg\LANGUAGE\menu.msgbnd.extract\FRPG\data\Msg\Data_LANGUAGE\Conversation_.fmg'
- Manually remove initial encoding ANSI chars up until dialogue begins.

DS2 
- Run Atvaark's BinderTool executable on: 'Dark Souls II Scholar of the First Sin\Game\GameDataEbl.bdt'
- Navigate to: 'Dark Souls II Scholar of the First Sin\GameDataEbl\menu\Text\LANGUAGE\talk\*.fmg'
- Manually remove initial encoding ANSI chars up until dialogue begins.

DS3 
- Run Atvaark's BinderTool executable on: 'Dark Souls III\Game\Data1.bdt'
- Navigate to: 'Dark Souls III\Game\Data1\msg\LANGUAGE\会話[_dlc1/2].fmg'
- Manually remove initial encoding ANSI chars up until dialogue begins.

ER 
- Run Atvaark's BinderTool executable on: 'Elden Ring\Game\Data0.bdt'
- Navigate to: 'Elden Ring\Game\Data0\msg\LANGUAGE\menu.msgbnd'
- Manually remove initial encoding ANSI chars up until dialogue begins.

___
__| For 'preprocessed_tk_al_cl_ed' |__
Make copies from 'preprocessed_tk_al_cl' to new dir and manually clean them up & manually fix remaining alignment issues.

___
__| Naming Conventions |__
tk = sentence tokenized<br>
al = aligned using hunalign<br>
cl = cleaned (from hunalign remains)<br>
ed = edited (manual cleanup and alignment work)