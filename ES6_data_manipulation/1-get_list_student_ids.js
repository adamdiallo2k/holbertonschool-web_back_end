function getListStudentIds(arrayOfStudents) {
  // Check if the argument is an array
  if (!Array.isArray(arrayOfStudents)) {
    return [];
  }
  const ids = arrayOfStudents.map(student => student.id);

  return ids;
}

export default getListStudentIds;
