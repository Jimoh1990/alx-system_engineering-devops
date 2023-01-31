#!/usr/bin/env ruby
# a regular expression that matches a certain pattern

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
