export function toCamelCase(str: string): string {
  let words = str.split(/[-_]/);

  let result = words[0];

  for (let i = 1; i < words.length; i++) {
    result += words[i][0].toUpperCase() + words[i].slice(1);
  }

  return result;
}
