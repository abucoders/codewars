export const findOdd = (xs: number[]): number => {
  for (let i=0; i< xs.length; i++){
    if(xs.filter(item => item === xs[i]).length % 2 !== 0){
      return xs[i];
    }
  }

  return 0;
};
