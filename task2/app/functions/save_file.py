def save_audio_file_to_db(db: Session, file: UploadFile):
    # сохраняем файл на диск и получаем его содержимое
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    data = open(file.filename, "rb").read()

    # сохраняем информацию о файле в базу данных
    db_file = models.AudioFile(
        filename=file.filename,
        content_type=file.content_type,
        data=data
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return db_file