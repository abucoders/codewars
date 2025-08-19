function generateHashtag(str) {
  if (!str || str.trim() === "") return false;

  const words = str.trim().split(/\s+/);

  const capitalizedWords = words.map(
    word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
  );

  const result = "#" + capitalizedWords.join("");

  return result.length > 140 ? false : result;
}
