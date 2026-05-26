import os
import shutil
import hashlib
import argparse
import logging
import zipfile
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

# =====================================
# INIT
# =====================================
init(autoreset=True)

# =====================================
# LOGGING
# =====================================
logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================================
# HASH FUNCTION
# =====================================
def sha256_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:

            for chunk in iter(
                lambda: f.read(4096),
                b""
            ):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception:
        return None

# =====================================
# COPY FILE
# =====================================
def copy_file(src, dst, dry_run=False):

    try:

        if dry_run:

            print(
                Fore.YELLOW +
                f"[DRY RUN] {src} -> {dst}"
            )

            return

        os.makedirs(
            os.path.dirname(dst),
            exist_ok=True
        )

        shutil.copy2(src, dst)

        print(
            Fore.GREEN +
            f"✔ Copied: {src}\n"
        )

        logging.info(
            f"Copied: {src}"
        )

    except Exception as e:

        logging.error(str(e))

        print(
            Fore.RED +
            f"✘ Failed: {src}"
        )
# =====================================
# COMPARE FILES
# =====================================
def file_changed(src, dst):

    if not os.path.exists(dst):
        return True

    return sha256_hash(src) != sha256_hash(dst)

# =====================================
# CREATE ZIP
# =====================================
def compress_backup(folder_path, zip_name):

    with zipfile.ZipFile(
        zip_name,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, _, files in os.walk(folder_path):

            for file in files:

                file_path = os.path.join(root, file)

                arcname = os.path.relpath(
                    file_path,
                    folder_path
                )

                zipf.write(file_path, arcname)

    print(
        Fore.CYAN +
        f"\n📦 Compressed: {zip_name}"
    )

# =====================================
# BACKUP ENGINE
# =====================================
def backup_folder(
    source,
    destination,
    dry_run=False,
    compress=False
):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_path = os.path.join(
        destination,
        f"backup_{timestamp}"
    )

    total_files = 0
    copied_files = 0

    print(
        Fore.BLUE +
        "\n🚀 BACKUP ENGINE STARTED\n"
    )

    with ThreadPoolExecutor(max_workers=5) as executor:

        futures = []

        for root, _, files in os.walk(source):

            for file in files:

                src_file = os.path.join(root, file)

                rel_path = os.path.relpath(
                    src_file,
                    source
                )

                dst_file = os.path.join(
                    backup_path,
                    rel_path
                )

                total_files += 1

                if file_changed(src_file, dst_file):

                    copied_files += 1

                    futures.append(
                        executor.submit(
                            copy_file,
                            src_file,
                            dst_file,
                            dry_run
                        )
                    )

        for future in futures:
            future.result()

    print(
        Fore.GREEN +
        "\n===== BACKUP SUMMARY ====="
    )

    print(f"Total Files Scanned : {total_files}")
    print(f"Files Backed Up     : {copied_files}")
    print(f"Backup Location     : {backup_path}")

    logging.info(
        f"Backup completed: {backup_path}"
    )

    if compress and not dry_run:

        zip_name = backup_path + ".zip"

        compress_backup(
            backup_path,
            zip_name
        )

# =====================================
# MAIN
# =====================================
def main():

    parser = argparse.ArgumentParser(
        description="Folder Backup Tool Ultra"
    )

    parser.add_argument(
        "-s",
        "--source",
        required=True,
        help="Source folder"
    )

    parser.add_argument(
        "-d",
        "--destination",
        required=True,
        help="Backup destination"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate backup"
    )

    parser.add_argument(
        "--compress",
        action="store_true",
        help="Compress backup"
    )

    args = parser.parse_args()

    backup_folder(
        args.source,
        args.destination,
        args.dry_run,
        args.compress
    )

# =====================================
# START
# =====================================
if __name__ == "__main__":
    main()
