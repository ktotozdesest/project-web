function up(id) {
    console.log(ss);
    console.log(sped);
    console.log(id);
    sped = sped + 110 ** id * 0.001;
    ss = ss - 100 ** id * 60;
}