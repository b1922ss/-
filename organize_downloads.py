#!/usr/bin/env python3
"""ダウンロードフォルダー整理スクリプト"""

import shutil
from pathlib import Path

BASE = Path("/Users/sigsig3636/Downloads")

moves = {
    "01_研究": [
        "0_JoSM_ResponseLetter_rm_1 (1).docx",
        "0_JoSM_ResponseLetter_rm_1.docx",
        "10thFoKCs_pos_shigeno_1.pdf",
        "1_JoSM_Manuscript_r1_Clean.pdf",
        "1_JoSM_Manuscript_r1_TrackChg.pdf",
        "1_JoSM_Manuscript_r2_colored.docx",
        "1_JoSM_Manuscript_r2_colored_recolored.docx",
        "1_JoSM_Manuscript_rm_1_clean.pdf",
        "1_0404_版_アサイン付き_品川ゼミスケジュール2026.docx",
        "1_アサイン付き_品川ゼミスケジュール2026.docx",
        "1_アサイン付き_品川ゼミスケジュール2026.pdf",
        "2_JoSM_Figures_rm_2.pdf",
        "4_JoSM_Supplementary_rm_2.pdf",
        "ACTORサイクル_プレゼン_0224.pdf",
        "Akaka元.docx",
        "Akaka新.docx",
        "CV_20260311_shogakuronso_103_4_63.pdf",
        "GS_AIアクタープレゼンr0.3_cowork (1).pdf",
        "GS_AIアクタープレゼンr0.3_cowork (1).pptx",
        "GS_AIアクタープレゼンr0.3_cowork.pptx",
        "GS_AIアクタープレゼンr0.3.pptx",
        "JOSM-08-2025-0377.R1_Proof_hi (1).pdf",
        "JOSM-08-2025-0377.R1_Proof_hi.pdf",
        "JP_changes_extracted_from_NC_v2.xlsx",
        "JoSM_改訂管理表 1 (1).xlsx",
        "Journal of Service Management - You've submitted your revised manuscript, here is what you can expect next - s.shigeno3@gmail.com - Gmail.pdf",
        "Journal of Service Management _ Emerald Publishing_files",
        "MSC研究計画01.pdf",
        "QUIS19_pre_EN_shigeno_11.pdf",
        "Quarterly159-41.pdf",
        "ResponseLetter_Sample (1).docx",
        "ResponseLetter_Sample.docx",
        "RevManage_Sample.xlsx",
        "ScholarOne Manuscripts.pdf",
        "al-Gehmanetal-2013-ValuesWorkAProcessStudyoftheEmergenceandPerformanceofOrganizationalValuesPractices.pdf",
        "diff_A_B.xlsx",
        "diff_report_A_B.md",
        "diff_report_A_B.txt",
        "gist-as-ks_博論骨子.pdf",
        "rp-as-ks_2430008_寺前環_Rev5.docx",
        "sfsconf_A00191_20260302_120709_certificate.pdf",
        "ssrn-2032112.pdf",
        "スライド原稿_all.pdf",
        "セルフケアにおけるアクター・エンゲージメントの研究.pptx (1).pdf",
        "セルフケアにおけるアクター・エンゲージメントの研究.pptx (2).pdf",
        "セルフケアにおけるアクター・エンゲージメントの研究.pptx.pdf",
        "坂口サービス学会2026_2-E-5-01.pdf",
        "かんたんVCC人事プレゼンr0.1-プロフ除き.pdf",
        "査読改訂.docx",
        "博士論文骨子_shigeno (1).pdf",
        "博士論文骨子_shigeno.pdf",
        "博論検討1.pdf",
        "博論章立て1.pdf",
        "2回目プレゼンv4_社名削除.pdf",
        "2回目プレゼンv3-expt2編集中.pdf",
        "2回目プレゼンv4.pdf",
        "20260228_Gehman2013_坂口_ファイルサイズ圧縮 (1).pptx",
        "20260228_Gehman2013_坂口_ファイルサイズ圧縮.pptx",
        "直観の経営 1.pdf",
        "【テキスト】ナラティブ・アプローチによる自己再発見.pdf",
        "研究1_garmin_.pptx",
        "論文骨子.docx",
        # フォルダ
        "JoSM1",
        "NC0214",
        "minor_research_shigeno",
        "書籍化",
    ],
    "02_ヨット": [
        "20251120_TAPSⅡ　船舶検査証書.pdf",
        "2026年度 TAPSⅡ　団体保険加入証.pdf",
        "202603 セイルマート.pdf",
        "56207IN ja.pdf",
        "56207IN.pdf",
        "84018OM.pdf",
        "Ancor1-ZX477_NMEA_2000_Basic_Installation.pdf",
        "B&G H5000マニュアル.pdf",
        "B&G H5000設置マニュアル.pdf",
        "B&G Vulcanはじめに.pdf",
        "B&G Vulcanクイックガイド.pdf",
        "B&G Vulcan操作マニュアル.pdf",
        "B&G Vulcan設定マニュアル.pdf",
        "BG H5000-1.pdf",
        "BG H5000-2.pdf",
        "DCCマニュアルUM_Dual_20Input_20DC-DC_20On-Board_20Battery_20Charger_20with_20MPPT_B2.pdf",
        "KSEC_2.pdf",
        "KSEC倫理審査申請書（研究計画・チェックリスト）2024年11月20日ver..xlsx",
        "RaceSchedule2026.pdf",
        "al-BGH5000-1.pdf",
        "al-BGH5000-1（結合済）.pdf",
        "al-BGH5000-2.pdf",
        "bg-triton-install-en.pdf",
        "en-us-Vulcan-Series_01_EN_QG_988-11560-003_w.pdf",
        "en-us-Vulcan-Series_GS_EN_988-11123-002_w.pdf",
        "en-us-Vulcan-Series_IM_EN_988-11099-004_w.pdf",
        "en-us-Vulcan-Series_OM_EN_005_w.pdf",
        "ksec_1.pdf",
        "インバーターマニュアルRIV1220P2-10S-JP-Manual-A1.4_10ee8a61-57a9-40bb-81e3-7e506dc9b242.pdf",
        "外洋艇セールナンバー登録規則ガイドライン.pdf",
        "外洋艇登録申込書_様式.xlsx",
        "外洋艇登録申込書_記入例.pdf",
        "横浜ミドルボートGWレガッタ参加申込書.docx",
        "配線図3-2重野修正.pdf",
        "配線図3.xlsx",
        "配線図（3-21）.xlsx",
        "艇登録停止届 2026.doc",
        # フォルダ
        "IORAH_12_4_19022026-0114332",
    ],
    "03_仕事": [
        "AI活用実践セミナー_20260311.pdf",
        "AI活用実践セミナーのご案内.pdf",
        "WTSS-SIG_発起人会議事録_20260311 (1).docx",
        "WTSS-SIG_発起人会議事録_20260311.docx",
        "WTSS-SIG_発起人会議事録_20260311_修正版.docx",
        "WTSS-SIG　mtg 20260311 2 (online-audio-converter.com).mp3",
        "ai_dx_service_proposal_20260404024242.pdf",
        "dc70f161-60ed-427b-bbd8-90091da5d54c_AI活用DX構築サービス（仮称）.pdf",
        "サービス学会 SIG 設立趣意書 r3_01.pdf",
        "サービス学会 SIG 設立趣意書 r4_01.pdf",
        "20260311_発起人会_前半カット.txt",
        "参加者へのご案内.docx",
        "参加者への説明文.pdf",
        "参加者への説明文_2.pdf",
        "働く人のためのセルフ・コンパッション6週間コース　2026年4月スタート _ Peatix.pdf",
        # フォルダ
        "勉強会02",
    ],
    "04_法務・相続": [
        "06_株主名簿（変更後）.docx",
        "Step1_05_株主名簿（変更後） 2.docx",
        "Step1_05_株主名簿（変更後）.docx",
        "TAPS会計書.xlsx",
        "TNN社_R7.12月期内訳書 1.pdf",
        "TNN社_R7.12月期決算書 1.pdf",
        "Team_CFO_手書きメモ.pdf",
        "_別記第5号様式(住所等変更届).rtf",
        "別記第5号様式(住所等変更届).rtf.rtfd",
        "登録停止届.doc",
        "登録停止届_記入例.pdf",
        "2026収支検討 4～6月改善方針.pdf",
        "運用中_実績入力_KMC様共有用_預金の流れ 1.xlsx",
        # フォルダ
        "TNN_株主変更_桑村氏",
        "TNN_決算書_全期",
        "TNN_決算書_全期 2",
        "TNN_第1期-第6期_決算書",
        "TNN_第1期-第6期_決算書 2",
        "ティルナ株主変更_H氏死去",
        "ティル・ナ・ノーグ_決算書（２期ー６期）",
    ],
    "05_医療・健康": [
        "ニコ20260315Joyさん受診.m4a",
    ],
    "06_写真・動画": [
        "IMG_3063.HEIC",
        "IMG_3150.HEIC",
        "IMG_3150.jpeg",
        "IMG_3151.HEIC",
        "IMG_3151.jpeg",
        "IMG_3159.JPG",
        "IMG_3298.HEIC",
        "IMG_3338.jpeg",
        "IMG_3404.jpeg",
        "IMG_3632.JPG",
        "IMG_3633.JPG",
        # フォルダ
        "Photos-1-001",
        "写真",
    ],
    "09_その他": [
        # zipファイル（Notionエクスポート等）
        "23199564-e15d-4ae6-9eed-fe9c7f59420d_ExportBlock-4ad9ab53-7057-4b8e-9c0e-271beca4bbbd.zip",
        "6fcc38aa-5c86-4d44-b2e5-6968c9691e8e_ExportBlock-845b5e85-330a-4c49-be9b-524aae28a5ff.zip",
        "8fab77b4-cf2d-4c54-9eb7-62e1b73c65e6_ExportBlock-b7a95d47-4735-4c47-a07e-9437fb5a6b72.zip",
        # メール
        "情報セキュリティ研修（e-ラーニング）の実施について_Cyber Security Training(e-learning) - RCACI _isc@ml.jaist.ac.jp_ - 2026-02-05 1657.eml",
        # その他ファイル
        "愛車検索（車種別ラインナップ） – エムリットフィルター｜MLITFILTER.pdf",
        # 内容不明ファイル
        "by2fy1y1.docx",
        "jm2.docx",
        # 翻訳文書（要確認）
        "1_元日.pdf",
        "1_元英.pdf",
        "1_新英.pdf",
        # 一時ファイル
        "~$HRM-r9.6.pptx",
        "~$JoSM_Manuscript_r1_redblue.docx",
        # フォルダ
        "attach",
        "attach-2",
        "OneDrive_1_2025-7-12",
        "既存ドキュメント",
        "注文書テンプレート青",
    ],
}


def move_item(src: Path, dest_dir: Path) -> str:
    if not src.exists():
        return f"  スキップ（存在しない）: {src.name}"
    dest = dest_dir / src.name
    if dest.exists():
        return f"  スキップ（移動先に既存）: {src.name}"
    shutil.move(str(src), str(dest))
    return f"  移動完了: {src.name}"


def main():
    moved = 0
    skipped = 0

    for folder, items in moves.items():
        dest_dir = BASE / folder
        if not dest_dir.exists():
            print(f"[警告] 移動先フォルダが存在しません: {folder}")
            continue
        print(f"\n📁 {folder}")
        for name in items:
            result = move_item(BASE / name, dest_dir)
            print(result)
            if "移動完了" in result:
                moved += 1
            else:
                skipped += 1

    print(f"\n✅ 完了: {moved} 件移動, {skipped} 件スキップ")


if __name__ == "__main__":
    main()
